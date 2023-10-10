"""2883. Drop Missing Data"""

import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(axis=0)
