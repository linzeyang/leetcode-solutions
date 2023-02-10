"""1550. Three Consecutive Odds"""

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        for idx in range(len(arr) - 2):
            if arr[idx] % 2 and arr[idx + 1] % 2 and arr[idx + 2] % 2:
                return True

        return False
