import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect("data/db/bluestock_mf.db")

df = pd.read_sql(
    "SELECT amfi_code, date, nav FROM nav_history",
    conn
)

# Convert date
df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

# Remove bad rows
df = df.dropna(subset=["date"])
df = df[df["nav"] > 0]

risk_data = []

for code in df["amfi_code"].unique():

    fund = df[df["amfi_code"] == code].copy()

    fund = fund.sort_values("date")

    fund["daily_return"] = fund["nav"].pct_change()

    fund = fund.dropna()

    if len(fund) < 2:
        volatility = 0
        sharpe = 0
    else:
        volatility = fund["daily_return"].std()

        if volatility == 0 or np.isnan(volatility):
            sharpe = 0
        else:
            sharpe = (
                fund["daily_return"].mean()
                / volatility
            )

    risk_data.append(
        [code, volatility, sharpe]
    )

risk_df = pd.DataFrame(
    risk_data,
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

print("\nRisk report saved.")

conn.close()