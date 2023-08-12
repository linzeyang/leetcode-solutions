"""1741. Find Total Time Spent by Each Employee"""

import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    df["day"] = employees["event_day"]
    df["emp_id"] = employees["emp_id"]
    df["total_time"] = employees["out_time"] - employees["in_time"]

    return df.groupby(["day", "emp_id"], as_index=False).sum()
