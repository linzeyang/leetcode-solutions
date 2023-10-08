"""2880. Select Data"""

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id == 101][["name", "age"]]
