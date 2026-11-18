import pandas as pd
import streamlit as st
import requests
from datetime import datetime, timezone
from streamlit_folium import st_folium

from src.quakes.loader import load_quake
from src.quakes.fetch import fetch_data
from src.quakes.filters import filter_quakes
from src.quakes.stats import (
    strongest_quake,
    quakes_per_day,
    average_depth,
    daily_summary,
)
from src.quakes.map_view import build_map

st.set_page_config(page_title="Earthquake Map", layout="wide")
st.title("Earthquakes registered last week")
st.caption("All times are in UTC")


@st.cache_data(ttl=600)
def get_data() -> pd.DataFrame:
    error = None
    try:
        fetch_data()
    except requests.RequestException as exc:
        error = str(exc)
    return load_quake(), datetime.now(timezone.utc), error


quakes, updated_at, fetch_error = get_data()

if fetch_error:
    st.warning("Could not reach USGS, showing the last saved data.")
st.caption(f"Data updated: {updated_at:%Y-%m-%d %H:%M} UTC")

first_day = quakes["time"].min().date()
last_day = quakes["time"].max().date()

st.sidebar.title("Filters")
min_mag = st.sidebar.slider(
    "Magnitude", min_value=2.5, max_value=7.0, value=4.0, step=0.1
)

dates = st.sidebar.date_input(
    "Earthquakes range",
    value=(first_day, last_day),
    min_value=first_day,
    max_value=last_day,
)

if len(dates) != 2:
    st.info("There must be a start and end date")
    st.stop()

start = pd.Timestamp(dates[0])
end = pd.Timestamp(dates[1]) + pd.Timedelta(days=1)

filtered = filter_quakes(quakes, min_mag=min_mag, start=start, end=end)

if filtered.empty:
    st.warning("There are not earthquakes with this filter")
    st.stop()


top = strongest_quake(filtered)
avg_depth = round(average_depth(df=filtered), 1)

col1, col2, col3 = st.columns(3)
col1.metric("Earthquakes", len(filtered))

col2.metric("Strongest earthquake", top["magnitude"])
col2.caption(top["location"])

col3.metric("Depth earthquake average", f"{avg_depth} km")

map_col, chart_col = st.columns([2, 1])

with map_col:
    st_folium(
        build_map(filtered),
        height=400,
    )
    st.caption(
        "🟢 Magnitude < 3   ·   🟠 Between 3 and 5   ·   🔴 5 or more   ·   Circle size depends on magnitude"
    )
with chart_col:
    st.subheader("Quakes per day")
    st.bar_chart(quakes_per_day(filtered))

with st.expander("Daily summary"):
    st.dataframe(daily_summary(filtered))
