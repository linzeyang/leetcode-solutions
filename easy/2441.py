"""2441. Largest Positive Integer That Exists With Its Negative"""

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ss = set()
        out = -1

        for num in nums:
            if (abss := abs(num)) in ss:
                continue

            ss.add(abss)

            if num < 0 and abss > out and abss in nums:
                out = abss
            elif num > 0 and num > out and -num in nums:
                out = num

        return out
