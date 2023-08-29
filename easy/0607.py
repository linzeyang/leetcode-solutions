"""607. Sales Person"""

import pandas as pd


def sales_person(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
    df = pd.merge(
        how="inner", left=orders, right=company, left_on="com_id", right_on="com_id"
    )

    reds = df[df["name"] == "RED"]

    return sales_person[~sales_person["sales_id"].isin(reds["sales_id"])][["name"]]
