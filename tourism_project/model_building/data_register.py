import pandas as pd
import os

# Define the path to the CSV file
CSV_PATH = "tourism_project/data/tourism.csv"
df = pd.read_csv(CSV_PATH)

# Define expected columns
EXPECTED_COLUMNS = ['CustomerID', 'ProdTaken', 'Age', 'TypeofContact', 'CityTier', 'Occupation', 'Gender', 'NumberOfPersonVisiting','NumberOfFollowups', 'ProductPitched', 'PreferredPropertyStar', 'MaritalStatus', 'NumberOfTrips', 'Passport', 'PitchSatisfactionScore', 'OwnCar', 'NumberOfChildrenVisiting', 'Designation', 'MonthlyIncome']

missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
if missing:
    raise ValueError(f"Dataset is missing expected columns: {missing}")

print("Dataset registered successfully.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("Columns:", list(df.columns))
print("Target distribution:")
print(df["ProdTaken"].value_counts())
