import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle

# Load Boston dataset
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

# Extract full data
X_full = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
y = raw_df.values[1::2, 2]

# Select required features
DIS = X_full[:, 7]
RM  = X_full[:, 5]
RAD = X_full[:, 8]
NOX = X_full[:, 4]

X = np.column_stack([DIS, RM, RAD, NOX])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale inputs
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Save both model + scaler
with open("house_price_model.pkl", "wb") as f:
    pickle.dump({"model": model, "scaler": scaler}, f)

print("Model trained + scaler saved successfully 🎉")
