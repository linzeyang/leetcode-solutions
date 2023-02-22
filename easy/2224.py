"""2224. Minimum Number of Operations to Convert Time"""

from datetime import datetime


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        diff = int(
            (
                datetime.strptime(correct, "%H:%M")
                - datetime.strptime(current, "%H:%M")
            ).total_seconds()
            // 60
        )

        out = 0

        for unit in (60, 15, 5):
            quo, rem = divmod(diff, unit)
            out += quo
            diff = rem

        out += rem

        return out
