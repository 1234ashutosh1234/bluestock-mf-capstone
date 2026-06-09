import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/nav_history_processed.csv"
)

pivot = df.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

corr = pivot.corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues"
)

plt.title("Fund Correlation Matrix")

plt.savefig(
    "reports/correlation_matrix.png"
)

print("Correlation Matrix saved.")