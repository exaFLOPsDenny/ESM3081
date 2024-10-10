import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset (Energy Efficiency Data Set)""
data = pd.read_csv("./HW2/data/parkinsons_updrs.csv")

# Displaying dataset info
print("Dataset shape:", data.shape)
print("Columns:", data.columns)

# Select features and target
X = data.iloc[:, 6:]  # First 8 columns as features
y = data.iloc[:, 4]   # Heating load as target (you can also use 'Cooling load')

# Check dataset dimensions
print(f"Number of data points: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")

# Splitting data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Test set size: {X_test.shape[0]} samples")

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define a function to train, predict, and evaluate the models
def train_and_evaluate_model(model, model_name):
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"\n{model_name} Performance:")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")

# Linear Regression
lr_model = LinearRegression()
train_and_evaluate_model(lr_model, "Linear Regression")

# Random Forest Regressor
rf_model = RandomForestRegressor(random_state=42)
train_and_evaluate_model(rf_model, "Random Forest")

# Gradient Boosting Regressor
gb_model = GradientBoostingRegressor(random_state=42)
train_and_evaluate_model(gb_model, "Gradient Boosting")

# Summarize performance of the models
print("\nModel comparison completed.")
