"""1507. Reformat Date"""

from datetime import datetime


class Solution:
    def reformatDate(self, date: str) -> str:
        date = (
            date.replace("th", "").replace("st", "").replace("nd", "").replace("rd", "")
        )
        return datetime.strptime(date, "%d %b %Y").strftime("%Y-%m-%d")
