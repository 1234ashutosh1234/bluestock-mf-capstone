import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/dashboard_summary_final.csv")

risk_free_rate = 0.05

sortino = []

for _, row in df.iterrows():

    downside_dev = row["volatility"] if row["volatility"] > 0 else 1

    ratio = (
        (row["return_pct"] - risk_free_rate)
        / downside_dev
    )

    sortino.append([
        row["amfi_code"],
        row["scheme_name"],
        round(ratio, 4)
    ])

result = pd.DataFrame(
    sortino,
    columns=[
        "amfi_code",
        "scheme_name",
        "sortino_ratio"
    ]
)

result.to_csv(
    "data/processed/sortino_ratio.csv",
    index=False
)

print(result)
print("\nSortino Ratio report saved.")