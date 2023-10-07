"""2878. Get the Size of a DataFrame"""

from typing import List

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players), len(players.columns)]
