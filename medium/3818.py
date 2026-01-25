"""3818. Minimum Prefix Removal to Make Array Strictly Increasing"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/
    Weekly Contest 486
    """

    def minimumPrefixLength(self, nums: List[int]) -> int:
        length: int = len(nums)

        if length == 1:
            return 0

        for idx in range(1, length):
            if nums[-idx - 1] >= nums[-idx]:
                break
        else:
            return 0

        return length - idx
