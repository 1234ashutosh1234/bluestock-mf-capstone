import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

df = pd.read_sql(
    "SELECT * FROM nav_history",
    conn
)

df["date"] = pd.to_datetime(
    df["date"],
    dayfirst=True,
    errors="coerce"
)

print("Missing dates:", df["date"].isna().sum())

df = df.sort_values(
    ["amfi_code", "date"]
)

# Daily Returns
df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
    .pct_change()
)

risk_report = []

for fund in df["amfi_code"].unique():

    temp = df[
        df["amfi_code"] == fund
    ].copy()

    temp = temp.dropna()

    volatility = (
        temp["daily_return"]
        .std()
        * np.sqrt(252)
    )

    sharpe = (
        temp["daily_return"]
        .mean()
        /
        temp["daily_return"].std()
    ) * np.sqrt(252)

    risk_report.append([
        fund,
        volatility,
        sharpe
    ])

risk_df = pd.DataFrame(
    risk_report,
    columns=[
        "amfi_code",
        "volatility",
        "sharpe_ratio"
    ]
)

print(risk_df)

risk_df.to_csv(
    "data/processed/risk_analysis.csv",
    index=False
)

print(
    "\nRisk report saved."
)

conn.close()