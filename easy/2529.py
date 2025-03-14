"""2529. Maximum Count of Positive Integer and Negative Integer"""

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0

        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1

        return max(pos, neg)
