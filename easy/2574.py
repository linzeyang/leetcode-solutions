"""2574. Left and Right Sum Differences"""

from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)

        out = []

        for val in nums:
            right_sum -= val
            out.append(abs(left_sum - right_sum))
            left_sum += val

        return out
