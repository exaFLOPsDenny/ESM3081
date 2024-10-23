import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo  # Import the dataset fetching function
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Fetch Dry Bean Dataset using ucimlrepo
dry_bean = fetch_ucirepo(id=602)

# Data (features and targets as pandas dataframes)
X = dry_bean.data.features
y = dry_bean.data.targets

# Handle missing values by dropping rows with missing values
X = X.dropna()
y = y.loc[X.index]  # Ensure targets match the remaining data points

# Encode class labels as integers
le = LabelEncoder()
y = le.fit_transform(y)

# Split data into training, validation, and test sets (60% train, 20% val, 20% test)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)  # 60% train
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)  # 20% val, 20% test

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Convert the data to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_val = torch.tensor(X_val, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
y_val = torch.tensor(y_val, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)

# Create DataLoader for PyTorch
batch_size = 32
train_dataset = TensorDataset(X_train, y_train)
val_dataset = TensorDataset(X_val, y_val)
test_dataset = TensorDataset(X_test, y_test)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# 2. Define Neural Network Model in PyTorch
class NeuralNet(nn.Module):
    def __init__(self, input_size, num_classes):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.dropout = nn.Dropout(0.5)  # Dropout layer for MC Dropout
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, num_classes)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Initialize the model, loss function, and optimizer
input_size = X_train.shape[1]
num_classes = len(np.unique(y_train))
model = NeuralNet(input_size, num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. Training Function
def train(model, train_loader, criterion, optimizer, epochs=50):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}")

# 4. Evaluation Function
def evaluate(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    return accuracy

# Train the model
train(model, train_loader, criterion, optimizer, epochs=512)

# Evaluate without reject option
accuracy = evaluate(model, test_loader)
print(f"Accuracy without reject option: {accuracy:.4f}")

# 5. Uncertainty Quantification

# 1. Confidence Uncertainty Measure
def confidence_uncertainty(softmax_probs):
    max_probs, _ = torch.max(softmax_probs, dim=1)
    return -max_probs

# 2. Margin Uncertainty Measure
def margin_uncertainty(softmax_probs):
    sorted_probs, _ = torch.sort(softmax_probs, dim=1, descending=True)
    margin = sorted_probs[:, 0] - sorted_probs[:, 1]
    return -margin

# 3. Entropy Uncertainty Measure
def entropy_uncertainty(softmax_probs):
    entropy = -torch.sum(softmax_probs * torch.log(softmax_probs + 1e-10), dim=1)  # Add small epsilon for numerical stability
    return entropy

# Get predictions and calculate uncertainties
def calculate_uncertainties(model, test_loader):
    model.eval()
    confidence_list = []
    margin_list = []
    entropy_list = []
    
    with torch.no_grad():
        for inputs, _ in test_loader:
            outputs = model(inputs)
            softmax_probs = F.softmax(outputs, dim=1)
            
            # Calculate uncertainties
            confidence_list.append(confidence_uncertainty(softmax_probs))
            margin_list.append(margin_uncertainty(softmax_probs))
            entropy_list.append(entropy_uncertainty(softmax_probs))
    
    # Convert lists to tensors
    confidence_uncertainty_tensor = torch.cat(confidence_list)
    margin_uncertainty_tensor = torch.cat(margin_list)
    entropy_uncertainty_tensor = torch.cat(entropy_list)
    
    return confidence_uncertainty_tensor, margin_uncertainty_tensor, entropy_uncertainty_tensor

# Run uncertainty calculations
confidence_uncertainty_vals, margin_uncertainty_vals, entropy_uncertainty_vals = calculate_uncertainties(model, test_loader)

# For example, let's print the first few uncertainty values
print("Confidence Uncertainty (first 5):", confidence_uncertainty_vals[:5])
print("Margin Uncertainty (first 5):", margin_uncertainty_vals[:5])
print("Entropy Uncertainty (first 5):", entropy_uncertainty_vals[:5])

# Function to test different thresholds for a given uncertainty measure
def optimize_threshold(uncertainty_vals, y_true, model, val_loader, num_thresholds=100):
    # Create thresholds between the min and max of uncertainty values
    range_min = uncertainty_vals.min().item()
    range_max = uncertainty_vals.max().item()
    
    thresholds = torch.linspace(range_min, range_max, num_thresholds)
    
    best_threshold = None
    best_accuracy = 0.0
    best_rejection_rate = 0.0

    for threshold in thresholds:
        accepted_idx = uncertainty_vals <= threshold  # Accept if uncertainty is below threshold
        rejected_idx = uncertainty_vals > threshold   # Reject if uncertainty is above threshold
        
        # Calculate accuracy for accepted samples
        accepted_samples = torch.nonzero(accepted_idx, as_tuple=True)[0]
        y_accepted = y_true[accepted_samples]

        if len(accepted_samples) > 0:
            correct = 0
            total = 0
            for i, (inputs, labels) in enumerate(val_loader):
                if i in accepted_samples:
                    outputs = model(inputs)
                    _, predicted = torch.max(outputs, 1)
                    total += labels.size(0)
                    correct += (predicted == labels).sum().item()
            accuracy = 100 * correct / total if total > 0 else 0.0
        else:
            accuracy = 0.0

        rejection_rate = 100 * (1 - len(accepted_samples) / len(uncertainty_vals))

        # Choose the best threshold based on accuracy
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_threshold = threshold
            best_rejection_rate = rejection_rate

    return best_threshold, best_accuracy, best_rejection_rate

# Apply the optimization for each uncertainty measure
def find_best_thresholds(model, val_loader, y_val):
    confidence_uncertainty_vals, margin_uncertainty_vals, entropy_uncertainty_vals = calculate_uncertainties(model, val_loader)
    
    print("Optimizing thresholds for uncertainty measures...")
    
    # Optimize thresholds for each uncertainty measure
    best_conf_threshold, best_conf_accuracy, best_conf_rejection_rate = optimize_threshold(confidence_uncertainty_vals, y_val, model, val_loader)
    best_margin_threshold, best_margin_accuracy, best_margin_rejection_rate = optimize_threshold(margin_uncertainty_vals, y_val, model, val_loader)
    best_entropy_threshold, best_entropy_accuracy, best_entropy_rejection_rate = optimize_threshold(entropy_uncertainty_vals, y_val, model, val_loader)

    print(f"Best Confidence Threshold: {best_conf_threshold:.4f}, Accuracy: {best_conf_accuracy:.4f}, Rejection Rate: {best_conf_rejection_rate:.2f}%")
    print(f"Best Margin Threshold: {best_margin_threshold:.4f}, Accuracy: {best_margin_accuracy:.4f}, Rejection Rate: {best_margin_rejection_rate:.2f}%")
    print(f"Best Entropy Threshold: {best_entropy_threshold:.4f}, Accuracy: {best_entropy_accuracy:.4f}, Rejection Rate: {best_entropy_rejection_rate:.2f}%")

# Run the threshold optimization on the validation set
find_best_thresholds(model, val_loader, y_val)