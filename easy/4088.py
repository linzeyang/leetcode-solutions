"""
4088. Difference Between Peaks and Valleys

https://leetcode.com/problems/difference-between-peaks-and-valleys/

Biweekly Contest 194
"""


class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak_sum: int = 0
        valley_sum: int = 0

        for idx in range(1, len(nums) - 1):
            num: int = nums[idx]

            if num > nums[idx - 1] and num > nums[idx + 1]:
                peak_sum += num
            elif num < nums[idx - 1] and num < nums[idx + 1]:
                valley_sum += num

        return peak_sum - valley_sum
