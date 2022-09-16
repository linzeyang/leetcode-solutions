"""
268. Missing Number
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Runtime: 188 ms, faster than 71.44% of Python3 online submissions for Missing Number.
        # Memory Usage: 15.7 MB, less than 6.85% of Python3 online submissions for Missing Number.
        all_nums = set(range(len(nums) + 1))

        for num in nums:
            all_nums.remove(num)

        return all_nums.pop()
