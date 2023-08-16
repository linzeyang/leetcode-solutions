"""1693. Daily Leads and Partners"""

import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(["date_id", "make_name"], as_index=False)[
        "lead_id"
    ].nunique()

    df["unique_leads"] = df["lead_id"]

    df["unique_partners"] = (
        daily_sales.groupby(["date_id", "make_name"])["partner_id"]
        .nunique()
        .reset_index()["partner_id"]
    )

    return df[["date_id", "make_name", "unique_leads", "unique_partners"]]
