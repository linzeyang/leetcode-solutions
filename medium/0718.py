"""718. Maximum Length of Repeated Subarray"""

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp: list[list[int]] = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for idx in range(1, len(nums1) + 1):
            for jdx in range(1, len(nums2) + 1):
                if nums1[idx - 1] == nums2[jdx - 1]:
                    dp[idx][jdx] = dp[idx - 1][jdx - 1] + 1

        return max(max(line) for line in dp)
