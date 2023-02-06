"""1385. Find the Distance Value Between Two Arrays"""

from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        out = 0

        for num1 in arr1:
            for num2 in arr2:
                if num1 - d <= num2 <= num1 + d:
                    break
            else:
                out += 1

        return out
