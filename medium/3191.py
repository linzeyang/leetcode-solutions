"""3191. Minimum Operations to Make Binary Array Elements Equal to One I"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        out = 0

        for idx in range(len(nums) - 2):
            if nums[idx]:
                continue

            for _ in range(3):
                nums[idx + _] = int(not nums[idx + _])

            out += 1

        return out if nums[-2] == nums[-1] == 1 else -1
