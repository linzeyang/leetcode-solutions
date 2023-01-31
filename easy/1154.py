"""1154. Day of the Year"""

from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        return datetime.strptime(date, "%Y-%m-%d").timetuple().tm_yday
