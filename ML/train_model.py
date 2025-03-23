import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib  # To save the trained model

# Load dataset
train_df = pd.read_csv("deadlock_dataset.csv")
test_df = pd.read_csv("deadlock_dataset.csv")

# Split features and labels
X_train, y_train = train_df.iloc[:, :-1], train_df["deadlock"]
X_test, y_test = test_df.iloc[:, :-1], test_df["deadlock"]

# Train Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(model, "deadlock_model.pkl")
print("Model saved as deadlock_model.pkl")
