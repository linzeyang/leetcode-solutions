"""586. Customer Placing the Largest Number of Orders"""

import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby("customer_number", as_index=False)["order_number"].nunique()

    return df[df["order_number"] == df.order_number.max()][["customer_number"]]
