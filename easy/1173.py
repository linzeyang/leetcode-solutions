"""1173. Immediate Food Delivery I"""

import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    ratio = round(
        len(delivery[delivery["order_date"] == delivery["customer_pref_delivery_date"]])
        / delivery.shape[0]
        * 100,
        2,
    )

    return pd.DataFrame([ratio], columns=["immediate_percentage"])
