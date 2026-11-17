import pandas as pd


def by_magnitud(df: pd.DataFrame, min_mag: float) -> pd.DataFrame:
    return df[df["magnitude"] >= min_mag]


def by_date_range(df: pd.DataFrame, start, end) -> pd.DataFrame:
    return df[(df["time"] >= start) & (df["time"] <= end)]


def filter_quakes(
    df, min_mag: float | None = None, start: None = None, end: None = None
) -> pd.DataFrame:
    result = df
    if min_mag is not None:
        result = by_magnitud(result, min_mag)
    if start is not None and end is not None:
        result = by_date_range(result, start, end)
    return result
