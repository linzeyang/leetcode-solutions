"""1907. Count Salary Categories"""

import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = len(accounts[accounts["income"] < 20_000])
    ave = len(accounts[(accounts["income"] >= 20_000) & (accounts["income"] <= 50_000)])
    hig = len(accounts[accounts["income"] > 50_000])

    return pd.DataFrame(
        {
            "category": ["Low Salary", "Average Salary", "High Salary"],
            "accounts_count": [low, ave, hig],
        }
    )
