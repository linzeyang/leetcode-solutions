"""2780. Minimum Index of a Valid Split"""

from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        length = len(nums)
        dominant = sorted(nums)[length // 2]
        count = nums.count(dominant)

        left, right = 0, count

        for idx in range(length - 1):
            if nums[idx] != dominant:
                continue

            left += 1
            right -= 1

            if left * 2 > idx + 1 and right * 2 > length - idx - 1:
                return idx

        return -1
