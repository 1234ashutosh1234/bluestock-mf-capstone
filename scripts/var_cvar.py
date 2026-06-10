import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/nav_history_processed.csv")

df["daily_return"] = pd.to_numeric(
    df["daily_return"],
    errors="coerce"
)

results = []

for code in df["amfi_code"].unique():

    temp = df[df["amfi_code"] == code]

    returns = temp["daily_return"].dropna()

    if len(returns) == 0:
        continue

    var_95 = np.percentile(returns, 5)

    cvar_95 = returns[
        returns <= var_95
    ].mean()

    results.append([
        code,
        round(var_95, 6),
        round(cvar_95, 6)
    ])

report = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "VaR_95",
        "CVaR_95"
    ]
)

report.to_csv(
    "data/processed/var_cvar_report.csv",
    index=False
)

print(report)
print("\nVaR & CVaR Report Saved.")