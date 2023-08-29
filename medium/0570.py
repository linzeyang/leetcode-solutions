"""570. Managers with at Least 5 Direct Reports"""

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby("managerId", as_index=False)["id"].count()

    managers = df[df["id"] >= 5]["managerId"]

    return employee[employee["id"].isin(managers)][["name"]]
