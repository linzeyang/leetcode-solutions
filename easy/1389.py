"""1389. Create Target Array in the Given Order"""

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        out = []

        for i in range(len(nums)):
            out.insert(index[i], nums[i])

        return out
