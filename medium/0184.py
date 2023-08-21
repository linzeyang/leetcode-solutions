"""184. Department Highest Salary"""

import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    df = pd.merge(
        how="inner",
        left=employee,
        right=department,
        left_on="departmentId",
        right_on="id",
    )

    df["max_sal"] = df.groupby("name_y")["salary"].transform("max")

    return df[df["salary"] == df["max_sal"]].rename(
        columns={"name_x": "Employee", "name_y": "Department", "salary": "Salary"},
        inplace=False,
    )[["Department", "Employee", "Salary"]]
