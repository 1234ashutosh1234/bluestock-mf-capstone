import pandas as pd

df = pd.read_csv(
    "data/processed/fund_performance.csv"
)

years = 1

df["cagr"] = (
    (df["end_nav"] / df["start_nav"])
    ** (1 / years)
    - 1
) * 100

df.to_csv(
    "data/processed/cagr_report.csv",
    index=False
)

print(df)