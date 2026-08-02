import pandas as pd
from sklearn.model_selection import train_test_split

CSV_PATH = "tourism_project/data/tourism.csv"
df = pd.read_csv(CSV_PATH)
df.drop(columns=['CustomerID', 'DurationOfPitch', 'Unnamed: 0'], errors="ignore", inplace=True)

# NOTE: 'Type' is intentionally left as raw strings (H/L/M).
# The training pipeline one-hot-encodes it, and the Streamlit app also sends
# raw H/L/M values. Encoding it here (e.g. LabelEncoder) would make training
# and serving use different representations, silently breaking predictions.

X = df.drop('ProdTaken', axis=1)
y = df['ProdTaken']

Xtrain, Xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

Xtrain.to_csv("Xtrain.csv", index=False)
Xtest.to_csv("Xtest.csv", index=False)
ytrain.to_csv("ytrain.csv", index=False)
ytest.to_csv("ytest.csv", index=False)

print("Data prepared: train/test splits written.")
