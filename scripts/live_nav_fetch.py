import requests
import pandas as pd
from pathlib import Path

# HDFC Top 100 Direct
scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    Path("data/raw/live_nav").mkdir(parents=True, exist_ok=True)

    nav_df.to_csv(
        "data/raw/live_nav/HDFC_Top100_NAV.csv",
        index=False
    )

    print("NAV data downloaded successfully")
    print(nav_df.head())

else:
    print("API Error:", response.status_code)