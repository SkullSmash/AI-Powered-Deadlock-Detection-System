import pandas as pd

df = pd.read_csv("/workspaces/AI-Powered-Deadlock-Detection-System/deadlock_dataset.csv")  # Ensure dataset.csv is in the ML folder
sample_features = df.iloc[0, :-1].tolist()  # Get first row (excluding 'deadlock' column)
print(sample_features)