"""2356. Number of Unique Subjects Taught by Each Teacher"""

import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby("teacher_id", as_index=False)["subject_id"].nunique()
    df["cnt"] = df["subject_id"]

    return df[["teacher_id", "cnt"]]
