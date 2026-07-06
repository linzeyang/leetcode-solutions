"""
3978. Unique Middle Element

https://leetcode.com/problems/unique-middle-element/description/

Biweekly Contest 186
"""

from collections import Counter


class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        counter: Counter[int] = Counter(nums)

        return counter[nums[len(nums) // 2]] == 1


class Solution2:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid_idx: int = len(nums) // 2
        target: int = nums[mid_idx]

        for idx, num in enumerate(nums):
            if num == target and idx != mid_idx:
                return False

        return True
