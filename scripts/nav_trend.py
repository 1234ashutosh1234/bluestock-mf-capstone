import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/nav_history_processed.csv")

df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(12,6))

for code in df["amfi_code"].unique():
    temp = df[df["amfi_code"] == code]
    plt.plot(temp["date"], temp["nav"], label=str(code))

plt.title("NAV Trend")
plt.xlabel("Date")
plt.ylabel("NAV")

plt.legend()

plt.savefig("reports/nav_trend.png")

print("NAV Trend saved.")