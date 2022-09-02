"""
11. Container With Most Water
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0

        left = 0
        right = len(height) - 1

        while left < right:
            if (area := (right - left) * min(height[left], height[right])) > result:
                result = area

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return result
