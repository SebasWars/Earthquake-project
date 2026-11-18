import pandas as pd
import folium


def color_for(number: int | float):
    if number < 3:
        return "green"
    elif number < 5:
        return "orange"
    return "red"


def build_map(df: pd.DataFrame) -> folium.Map:
    quake_map = folium.Map(location=[20, 0], zoom_start=2)

    for row in df.itertuples(index=False):
        magnitude_color = color_for(row.magnitude)
        folium.CircleMarker(
            location=(row.lat, row.lon),
            ttooltip=f"M{row.magnitude} · {row.depth} km · {row.time:%d %b %H:%M}",
            popup=folium.Popup(
                f"<b>{row.location}</b><br>"
                f"Magnitude: {row.magnitude}<br>"
                f"Depth: {row.depth} km<br>"
                f"Time (UTC): {row.time:%Y-%m-%d %H:%M}",
                max_width=250,
            ),
            radius=max(row.magnitude, 0.5) * 3,
            color=magnitude_color,
            fill=True,
            fill_color=magnitude_color,
            fill_opacity=0.6,
        ).add_to(quake_map)

    return quake_map
