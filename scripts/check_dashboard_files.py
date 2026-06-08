import pandas as pd

files = [
    "data/processed/dashboard_summary.csv",
    "data/processed/dashboard_summary_final.csv",
    "data/processed/fund_performance.csv",
    "data/processed/risk_analysis.csv"
]

for file in files:
    print("\n" + "="*60)
    print(file)

    try:
        df = pd.read_csv(file)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nShape:")
        print(df.shape)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print("ERROR:", e)