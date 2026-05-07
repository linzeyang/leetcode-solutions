"""
2033. Minimum Operations to Make a Uni-Value Grid

https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

Weekly Contest 262
"""

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums: list[int] = []

        for row in grid:
            nums.extend(row)

        nums.sort()

        target: int = nums[len(nums) // 2]
        rem: int = nums[0] % x
        out: int = 0

        for num in nums:
            if num % x != rem:
                return -1

            out += abs(num - target) // x

        return out
