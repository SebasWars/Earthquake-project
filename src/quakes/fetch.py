import json
import requests
from pathlib import Path

PATH = Path("data/data.json")

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": "2026-11-09",
    "endtime": "2026-11-16",
    "minmagnitude": 2.5,
}


def fetch_data() -> None:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    with open(PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

fetch_data()
