import requests
import pandas as pd
from pathlib import Path

funds = {
    "HDFC_Top100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_LargeCap": "118632",
    "Kotak_Bluechip": "120841"
}

Path("data/raw/live_nav").mkdir(
    parents=True,
    exist_ok=True
)

for name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(
                data["data"]
            )

            df.to_csv(
                f"data/raw/live_nav/{name}.csv",
                index=False
            )

            print(f"{name} downloaded")

        else:
            print(
                f"Failed {name}"
            )

    except Exception as e:
        print(e)

print("Finished")