"""
35. Search Insert Position
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return find_index(nums, 0, len(nums) - 1, target)


def find_index(array: List[int], head: int, tail: int, target: int) -> int:
    if head == tail:
        if array[head] >= target:
            return head
        return head + 1

    if (diff := tail - head) % 2:
        mid_left = head + int((diff - 1) / 2)
        mid_right = mid_left + 1

        if array[mid_left] > target:
            return find_index(array, head, mid_left, target)
        if array[mid_left] == target:
            return mid_left
        if array[mid_right] == target:
            return mid_right
        return find_index(array, mid_right, tail, target)
    else:
        mid = head + int(diff / 2)

        if array[mid] == target:
            return mid
        if array[mid] > target:
            return find_index(array, head, mid - 1, target)
        return find_index(array, mid + 1, tail, target)
