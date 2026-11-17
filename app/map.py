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
        magnitud_color = color_for(row.magnitud)
        folium.CircleMarker(
            location=(row.lat, row.lon),
            tooltip=f"Magnitud {row.magnitud} - {row.location}",
            radius=max(row.magnitud, 0.5) * 3,
            color=magnitud_color,
            fill=True,
            fill_color=magnitud_color,
            fill_opacity=0.6,
        ).add_to(last_quake)

    last_quake.save("index.html")
