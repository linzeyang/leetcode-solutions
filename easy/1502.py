"""1502. Can Make Arithmetic Progression From Sequence"""

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True

        arr = sorted(arr)
        diff = arr[1] - arr[0]

        for idx in range(2, len(arr)):
            if arr[idx] - arr[idx - 1] != diff:
                return False

        return True
