"""1527. Patients With a Condition"""

import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients.apply(lambda row: is_diab_1(row["conditions"]), axis=1)]


def is_diab_1(conditions: str) -> bool:
    out = False

    for cond in conditions.split():
        if cond.startswith("DIAB1"):
            out = True
            break

    return out
