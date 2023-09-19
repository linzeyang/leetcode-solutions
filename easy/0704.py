"""704. Binary Search"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bin_search(nums, target, 0, len(nums) - 1)


def bin_search(nums: list[int], target: int, left: int, right: int) -> int:
    if not nums or left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return bin_search(nums, target, left, mid - 1)

    return bin_search(nums, target, mid + 1, right)
