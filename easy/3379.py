"""3379. Transformed Array"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/transformed-array/
    Weekly Contest 427
    """

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length: int = len(nums)

        return [nums[(idx + num) % length] for idx, num in enumerate(nums)]
