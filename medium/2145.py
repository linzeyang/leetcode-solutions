"""2145. Count the Hidden Sequences"""

from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        offset = minn = maxx = 0

        for diff in differences:
            offset += diff

            maxx = max(maxx, offset)
            minn = min(minn, offset)

        max_diff = maxx - minn

        if upper - lower >= max_diff:
            return upper - lower - max_diff + 1

        return 0
