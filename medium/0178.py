"""178. Rank Scores"""

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    return scores.sort_values("score", ascending=False).assign(
        rank=lambda x: x.score.rank(method="dense", ascending=False).astype(int)
    )[["score", "rank"]]
