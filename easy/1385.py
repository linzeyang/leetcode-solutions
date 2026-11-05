"""
1385. Find the Distance Value Between Two Arrays

https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

Biweekly Contest 22
"""

from bisect import bisect_left
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        out = 0

        for num1 in arr1:
            idx: int = bisect_left(arr2, num1)

            if idx == 0:
                if arr2[0] - num1 > d:
                    out += 1
            elif idx == len(arr2):
                if num1 - arr2[-1] > d:
                    out += 1
            elif num1 - arr2[idx - 1] > d and arr2[idx] - num1 > d:
                out += 1

        return out
