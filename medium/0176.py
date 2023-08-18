"""176. Second Highest Salary"""

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    uni = employee["salary"].unique()

    if len(uni) < 2:
        return pd.DataFrame([None], columns=["SecondHighestSalary"])

    return pd.DataFrame([sorted(uni)[-2]], columns=["SecondHighestSalary"])
