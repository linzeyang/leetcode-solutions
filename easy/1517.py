"""1517. Find Users With Valid E-Mails"""

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users.apply(lambda row: verify(row["mail"]), axis=1)]


def verify(email: str) -> bool:
    if not email[0].isalpha():
        return False

    if email.count("@") > 1:
        return False

    if not email.endswith("@leetcode.com"):
        return False

    for char in email.split("@")[0]:
        if not (char.isalnum() or char in ("_", ".", "-")):
            return False

    return True
