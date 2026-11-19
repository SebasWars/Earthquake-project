from .config import DATA_PATH

from datetime import date, timedelta
import json
import requests

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

def fetch_data(days: int = 7) -> None:
    end = date.today()
    start = end - timedelta(days=days)
    params = {
        "format": "geojson",
        "starttime": start.isoformat(),
        "endtime": end.isoformat(),
        "minmagnitude": 2.5,
    }

    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    fetch_data()
