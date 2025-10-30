"""3354. Make Array Elements Equal to Zero"""

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """
        Prefix sum approach to count valid selections.

        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - only using a few integer variables
        """

        left_sum: int = 0
        right_sum: int = sum(nums)

        out: int = 0

        for num in nums:
            if num:  # Positive integer
                left_sum += num
                right_sum -= num
            elif abs(left_sum - right_sum) == 1:
                out += 1
            elif left_sum == right_sum:
                out += 2

        return out
