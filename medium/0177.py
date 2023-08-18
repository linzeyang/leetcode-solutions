"""177. Nth Highest Salary"""

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N > len(employee):
        return pd.DataFrame([None])

    uni = employee["salary"].unique()

    if N > len(uni):
        return pd.DataFrame([None])

    return pd.DataFrame([sorted(uni)[-N]])
