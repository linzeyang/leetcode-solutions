"""
303. Range Sum Query - Immutable
"""
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self._nums = nums

    def sumRange(self, left: int, right: int) -> int:
        # Runtime: 1897 ms, faster than 16.16% of Python3 online submissions for Range Sum Query - Immutable.
        # Memory Usage: 17.5 MB, less than 65.34% of Python3 online submissions for Range Sum Query - Immutable.
        return sum(self._nums[left : right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
