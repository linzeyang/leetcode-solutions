"""
169. Majority Element
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Runtime: 212 ms, faster than 74.30% of Python3 online submissions for Majority Element.
        # Memory Usage: 15.5 MB, less than 85.92% of Python3 online submissions for Majority Element.
        length = len(nums)

        if length in {1, 2}:
            return nums[0]

        half = length // 2
        temp = dict()

        for num in nums:
            if num not in temp:
                temp[num] = 1
            elif temp[num] + 1 <= half:
                temp[num] += 1
            else:
                return num
