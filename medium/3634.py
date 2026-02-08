"""3634. Minimum Removals to Balance Array"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-removals-to-balance-array/
    Biweekly Contest 162
    """

    def minRemoval(self, nums: List[int], k: int) -> int:
        length: int = len(nums)

        nums.sort()

        current_max: int = 0
        right: int = 0

        for left in range(length):
            while right < length:
                if nums[left] * k < nums[right]:
                    break

                current_max = max(current_max, right - left + 1)
                right += 1

        return length - current_max
