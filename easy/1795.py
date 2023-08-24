"""1795. Rearrange Products Table"""

import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df = products.melt(
        id_vars="product_id",
        value_vars=["store1", "store2", "store3"],
        value_name="price",
    )

    df = df[df["price"].notnull()]

    df.rename(columns={"variable": "store"}, inplace=True)

    return df[["product_id", "store", "price"]]
