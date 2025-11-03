"""3727. Maximum Alternating Sum of Squares"""

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        length: int = len(nums)

        if length == 1:
            return nums[0] ** 2

        nums.sort(key=abs, reverse=True)

        if length & 1:
            pivot: int = (length >> 1) + 1
        else:
            pivot: int = length >> 1

        return sum(num**2 for num in nums[:pivot]) - sum(num**2 for num in nums[pivot:])
