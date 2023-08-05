"""1873. Calculate Special Bonus"""

import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * (
        employees["employee_id"].astype(int).mod(2)
        & ~employees["name"].str.startswith("M")
    )

    return employees[["employee_id", "bonus"]].sort_values("employee_id")
