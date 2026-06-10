import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/nav_history_processed.csv"
)

df["daily_return"] = pd.to_numeric(
    df["daily_return"],
    errors="coerce"
)

plt.figure(figsize=(10,6))

for code in df["amfi_code"].unique():

    temp = df[
        df["amfi_code"] == code
    ].copy()

    rolling_mean = (
        temp["daily_return"]
        .rolling(2)
        .mean()
    )

    rolling_std = (
        temp["daily_return"]
        .rolling(2)
        .std()
    )

    sharpe = (
        rolling_mean /
        rolling_std
    )

    plt.plot(
        sharpe,
        label=str(code)
    )

plt.title(
    "Rolling Sharpe Ratio"
)

plt.xlabel("Observations")

plt.ylabel("Sharpe Ratio")

plt.legend()

plt.savefig(
    "reports/rolling_sharpe_chart.png"
)

print(
    "Rolling Sharpe Chart Saved."
)