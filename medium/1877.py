"""1877. Minimize Maximum Pair Sum in Array"""

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ll = sorted(nums)

        return max((ll[i] + ll[-i - 1]) for i in range(len(nums) // 2))
