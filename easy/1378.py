"""1378. Replace Employee ID With The Unique Identifier"""

import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    df = pd.merge(
        left=employees, right=employee_uni, how="left", left_on="id", right_on="id"
    )

    return df[["unique_id", "name"]]
