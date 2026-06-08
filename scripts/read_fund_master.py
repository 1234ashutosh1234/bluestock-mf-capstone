import pandas as pd

df = pd.read_csv("data/raw/fund_master.csv")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())