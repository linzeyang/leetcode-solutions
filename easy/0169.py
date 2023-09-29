"""169. Majority Element"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)

        if length < 3:
            return nums[0]

        half = length // 2
        temp = {}

        for num in nums:
            if num not in temp:
                temp[num] = 1
            elif temp[num] + 1 <= half:
                temp[num] += 1
            else:
                return num


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums) // 2]
