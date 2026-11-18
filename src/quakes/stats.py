import pandas as pd

def strongest_quake(df: pd.DataFrame):
    return df.loc[df["magnitude"].idxmax()]


def average_depth(df: pd.DataFrame):
    return df["depth"].mean()


def quakes_per_day(df: pd.DataFrame):
    return df.groupby(df["time"].dt.date).size()


def daily_summary(df: pd.DataFrame):
    return df.groupby(df["time"].dt.date).agg(
        count=("magnitude", "size"),
        max_mag=("magnitude", "max"),
        average_mag=("magnitude", "mean"),
    )
