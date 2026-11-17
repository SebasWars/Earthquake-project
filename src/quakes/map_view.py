import pandas as pd
import folium

def color_for(number: int | float):
    if number < 3:
        return "green"
    elif number < 5:
        return "orange"
    return "red"


def build_map(df: pd.DataFrame) -> folium.Map:
    last_quake = folium.Map(location=[20, 0], zoom_start=2)

    for row in df.itertuples(index=False):
        magnitude_color = color_for(row.magnitude)
        folium.CircleMarker(
            location=(row.lat, row.lon),
            tooltip=f"Magnitude {row.magnitude} - {row.location}",
            radius=max(row.magnitude, 0.5) * 3,
            color=magnitude_color,
            fill=True,
            fill_color=magnitude_color,
            fill_opacity=0.6,
        ).add_to(last_quake)

    last_quake.save("index.html")
