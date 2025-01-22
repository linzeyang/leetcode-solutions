"""2239. Find Closest Number to Zero"""

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        candidate = nums[0]
        candidate_distance = abs(candidate)

        for idx in range(1, len(nums)):
            num = nums[idx]

            if abs(num) < candidate_distance or (
                abs(num) == candidate_distance and num > 0
            ):
                candidate = num
                candidate_distance = abs(num)

        return candidate
