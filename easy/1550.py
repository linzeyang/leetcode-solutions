"""1550. Three Consecutive Odds"""

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        idx = 0

        while idx < len(arr) - 2:
            if arr[idx] & 1 == 0:
                idx += 1
                continue

            if arr[idx + 1] & 1 == 0:
                idx += 2
                continue

            if arr[idx + 2] & 1 == 0:
                idx += 3
                continue

            return True

        return False
