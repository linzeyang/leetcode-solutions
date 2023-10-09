"""2882. Drop Duplicate Rows"""

import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(["email"], keep="first")
