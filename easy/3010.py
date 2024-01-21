"""3010. Divide an Array Into Subarrays With Minimum Cost I"""

from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)

        regional_mins: list[int] = [0] * len(nums)
        regional_mins[-1] = regional_min = nums[-1]

        for idx in range(2, len(nums) - 1):
            if nums[-idx] < regional_min:
                regional_min = nums[-idx]

            regional_mins[-idx] = regional_min

        min_sum = nums[1] + regional_mins[2]

        for idx in range(2, len(nums) - 1):
            if nums[idx] + regional_mins[idx + 1] < min_sum:
                min_sum = nums[idx] + regional_mins[idx + 1]

        return nums[0] + min_sum
