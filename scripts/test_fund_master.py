import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())