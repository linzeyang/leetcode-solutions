"""153. Find Minimum in Rotated Sorted Array"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] < nums[0]:
                right -= 1
            else:
                left += 1

        return min(nums[0], nums[-1])
