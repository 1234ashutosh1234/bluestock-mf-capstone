import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/dashboard_summary.csv"
)

# Remove NaN rows
df = df.dropna()

# Top Returns Chart
plt.figure(figsize=(8,5))

plt.bar(
    df["amfi_code"].astype(str),
    df["sharpe_ratio"]
)

plt.title("Sharpe Ratio by Fund")
plt.xlabel("AMFI Code")
plt.ylabel("Sharpe Ratio")

plt.tight_layout()

plt.savefig(
    "reports/sharpe_ratio.png"
)

plt.show()