"""3220. Odd and Even Transactions"""

import pandas as pd


def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["odd_even"] = transactions["amount"].apply(
        lambda x: "odd" if x % 2 == 1 else "even"
    )

    grouped = (
        transactions.groupby(["transaction_date", "odd_even"])["amount"]
        .sum()
        .unstack(fill_value=0)
        .reset_index()
    )

    grouped.rename(columns={"odd": "odd_sum", "even": "even_sum"}, inplace=True)

    result = (
        grouped[["transaction_date", "odd_sum", "even_sum"]]
        .sort_values("transaction_date")
        .reset_index(drop=True)
    )

    return result
