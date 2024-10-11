import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler, QuantileTransformer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset (Parkinson's UPDRS dataset)
data = pd.read_csv("assignment/HW2/data/parkinsons_updrs.csv")

# Displaying dataset info
print("Dataset shape:", data.shape)

# Select features and target
X = data.iloc[:, 6:]  # Columns after the 6th as features
y = data.iloc[:, 4]   # motor_UPDRS as target


# Set the plot size for better visibility
plt.figure(figsize=(8, 6))

# Use seaborn's distplot to show both histogram and KDE (Kernel Density Estimation)
sns.histplot(y, kde=True, bins=30, color='blue')

# Add labels and title
plt.title("Distribution of Motor UPDRS Scores", fontsize=16)
plt.xlabel("Motor UPDRS", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# Display the plot
plt.show()

# Check dataset dimensions
print(f"Number of data points: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")

# Splitting data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Test set size: {X_test.shape[0]} samples")


# MinMax Scaling
minmax_scaler = MinMaxScaler()
X_train_scaled = minmax_scaler.fit_transform(X_train)
X_test_scaled = minmax_scaler.transform(X_test)

# Define a function to train, predict, and evaluate the models
def train_and_evaluate_model(model, model_name):
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"\n{model_name} Performance:")
    print(f"Mean Squared Error (MSE): {mse}")

# Define model hyperparameter tuning and cross-validation

# Random Forest hyperparameters
rf_params = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

# Gradient Boosting hyperparameters
gb_params = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.001, 0.01, 0.1],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

# Hyperparameter tuning using RandomizedSearchCV for Random Forest
rf_model = RandomForestRegressor(random_state=42)
rf_random = RandomizedSearchCV(estimator=rf_model, param_distributions=rf_params, 
                               n_iter=10, cv=5, random_state=42, n_jobs=-1)
train_and_evaluate_model(rf_random, "Random Forest (Tuned)")

# Hyperparameter tuning using RandomizedSearchCV for Gradient Boosting
gb_model = GradientBoostingRegressor(random_state=42)
gb_random = RandomizedSearchCV(estimator=gb_model, param_distributions=gb_params, 
                               n_iter=10, cv=5, random_state=42, n_jobs=-1)
train_and_evaluate_model(gb_random, "Gradient Boosting (Tuned)")

# Linear Regression
lr_model = LinearRegression()
train_and_evaluate_model(lr_model, "Linear Regression")


# Train, predict, and evaluate the models
def train_and_evaluate_model(model, model_name):
    # Fit the model with training data (for RandomizedSearchCV, it also performs hyperparameter tuning)
    model.fit(X_train_scaled, y_train)
    
    # Best model from RandomizedSearchCV
    if hasattr(model, 'best_estimator_'):
        print(f"Best hyperparameters for {model_name}: {model.best_params_}")
        model = model.best_estimator_  # Update model to best estimator after tuning
    
    # Predict on the test set
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    
    # Print results
    print(f"\n{model_name} Performance:")
    print(f"Mean Squared Error (MSE): {mse}")

# Hyperparameter tuning using RandomizedSearchCV for Random Forest
rf_model = RandomForestRegressor(random_state=42)
rf_random = RandomizedSearchCV(estimator=rf_model, param_distributions=rf_params, 
                               n_iter=10, cv=5, random_state=42, n_jobs=-1)

# Tune and evaluate Random Forest
train_and_evaluate_model(rf_random, "Random Forest (Tuned)")

# Hyperparameter tuning using RandomizedSearchCV for Gradient Boosting
gb_model = GradientBoostingRegressor(random_state=42)
gb_random = RandomizedSearchCV(estimator=gb_model, param_distributions=gb_params, 
                               n_iter=10, cv=5, random_state=42, n_jobs=-1)

# Tune and evaluate Gradient Boosting
train_and_evaluate_model(gb_random, "Gradient Boosting (Tuned)")

# Evaluate Linear Regression
lr_model = LinearRegression()
train_and_evaluate_model(lr_model, "Linear Regression")
