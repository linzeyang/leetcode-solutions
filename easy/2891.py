"""2891. Method Chain"""

import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(
        "weight", axis=0, ascending=False
    )[["name"]]
