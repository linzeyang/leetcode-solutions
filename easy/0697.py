"""697. Degree of an Array"""

from collections import Counter
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cc = Counter(nums)
        degree = max(cc.values())

        if degree == 1:
            return 1

        targets = {num for num, val in cc.items() if val == degree}
        temp = {}

        for idx, num in enumerate(nums):
            if num not in targets:
                continue

            if num not in temp:
                temp[num] = [idx, None]
            else:
                temp[num][-1] = idx

        return min(lis[-1] - lis[0] + 1 for lis in temp.values())
