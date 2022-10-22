"""2239. Find Closest Number to Zero"""

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ll = sorted(nums, key=abs)

        base = None
        candi = []

        for num in ll:
            if base is None:
                base = abs(num)
                candi.append(num)
            elif abs(num) == base:
                candi.append(num)
            else:
                break

        return max(candi)
