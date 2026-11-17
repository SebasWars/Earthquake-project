from pathlib import Path
import pandas as pd
import json

PATH = Path("data/data.json")

def load_quake(path: Path = PATH) -> pd.DataFrame:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    raw = pd.json_normalize(data["features"])

    coor = pd.DataFrame(
        raw["geometry.coordinates"].to_list(), columns=["lon", "lat", "depth"]
    )
    quakes = pd.DataFrame(
        {
            "location": raw["properties.place"],
            "time": pd.to_datetime(raw["properties.time"], unit="ms"),
            "magnitude": raw["properties.mag"],
        }
    )

    quakes = pd.concat([quakes, coor], axis=1)
    quakes = quakes.dropna(subset=["magnitud"])

    return quakes
