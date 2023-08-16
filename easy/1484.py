"""1484. Group Sold Products By The Date"""

import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby("sell_date", as_index=False)["product"].nunique()

    df["num_sold"] = df["product"]

    df["products"] = (
        activities.groupby("sell_date")
        .agg({"product": "unique"})["product"]
        .apply(sorted)
        .apply(lambda ps: ",".join(ps))
        .reset_index()["product"]
    )

    return df[["sell_date", "num_sold", "products"]]
