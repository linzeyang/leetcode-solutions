"""1148. Article Views I"""

import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        pd.unique(views[views.author_id.eq(views.viewer_id)]["author_id"]),
        columns=["id"],
    ).sort_values("id", inplace=False)
