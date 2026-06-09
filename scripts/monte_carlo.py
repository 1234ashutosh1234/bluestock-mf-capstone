import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/dashboard_summary_final.csv")

fund = df.iloc[0]

current_nav = fund["end_nav"]

simulations = 100

days = 252 * 5

mu = 0.12
sigma = 0.15

results = []

for i in range(simulations):

    prices = [current_nav]

    for _ in range(days):

        shock = np.random.normal(
            mu / 252,
            sigma / np.sqrt(252)
        )

        prices.append(
            prices[-1] * (1 + shock)
        )

    results.append(prices)

plt.figure(figsize=(10,6))

for sim in results:
    plt.plot(sim, alpha=0.2)

plt.title("Monte Carlo Simulation")

plt.xlabel("Days")
plt.ylabel("NAV")

plt.savefig(
    "reports/monte_carlo.png"
)

print("Monte Carlo chart saved")