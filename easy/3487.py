"""3487. Maximum Unique Subarray Sum After Deletion"""

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_set: set[int] = set(nums)

        sum_of_positives = sum(num for num in nums_set if num > 0)

        return sum_of_positives if sum_of_positives else max(nums_set)
