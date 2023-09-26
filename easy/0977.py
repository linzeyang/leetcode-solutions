"""977. Squares of a Sorted Array"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out: list[int] = []

        left, right = 0, len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                out.append(nums[left] ** 2)
                left += 1
            else:
                out.append(nums[right] ** 2)
                right -= 1

        return out[::-1]
