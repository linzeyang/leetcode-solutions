"""268. Missing Number"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = set(range(len(nums) + 1))

        for num in nums:
            all_nums.remove(num)

        return all_nums.pop()
