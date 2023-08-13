"""511. Game Play Analysis I"""

import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby("player_id", as_index=False)["event_date"].min()
    df["first_login"] = df["event_date"]

    return df[["player_id", "first_login"]]
