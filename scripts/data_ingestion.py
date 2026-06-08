import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
nav_history["date"] = pd.to_datetime(nav_history["date"])

# Sort values
nav_history = nav_history.sort_values(
    ["amfi_code", "date"]
)

# Calculate daily returns
nav_history["daily_return"] = (
    nav_history.groupby("amfi_code")["nav"]
    .pct_change()
)

nav_history["daily_return"] = nav_history["daily_return"].fillna(0)

print(nav_history.head(10))

# Save processed file
nav_history.to_csv(
    "data/processed/nav_history_processed.csv",
    index=False
)

print("Processed file saved successfully")