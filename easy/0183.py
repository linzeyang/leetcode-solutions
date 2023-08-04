"""183. Customers Who Never Order"""

import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers.id.isin(orders["customerId"])]

    result["Customers"] = result["name"]

    return result[["Customers"]]
