"""2082. The Number of Rich Customers"""

import pandas as pd


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        [len(store[store["amount"] > 500]["customer_id"].unique())],
        columns=["rich_count"],
    )
