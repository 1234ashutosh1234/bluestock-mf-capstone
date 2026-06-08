import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect("data/db/bluestock_mf.db")

query = """
SELECT
    amfi_code,
    MIN(nav) AS start_nav,
    MAX(nav) AS end_nav
FROM nav_history
GROUP BY amfi_code
"""

df = pd.read_sql(query, conn)

# Avoid division by zero
df["return_pct"] = np.where(
    df["start_nav"] > 0,
    ((df["end_nav"] - df["start_nav"]) / df["start_nav"]) * 100,
    None
)

print(df)

df.to_csv(
    "data/processed/fund_performance.csv",
    index=False
)

print("\nPerformance report saved.")

conn.close()