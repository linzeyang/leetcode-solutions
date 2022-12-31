"""704. Binary Search"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)

        if length == 0:
            return -1

        if length == 1:
            return 0 if nums[0] == target else -1

        mid = length // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return self.search(nums[:mid], target)

        res = self.search(nums[mid + 1:], target)

        if res == -1:
            return -1

        return mid + 1 + res
