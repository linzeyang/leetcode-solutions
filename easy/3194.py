"""3194. Minimum Average of Smallest and Largest Elements"""

from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        out = 51  # The largest number in nums is 50

        nums.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            if (avg := (nums[left] + nums[right]) / 2) < out:
                out = avg

            left += 1
            right -= 1

        return out
