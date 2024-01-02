"""2966. Divide Array Into Arrays With Max Difference"""

from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) < 3:
            return []

        out: list[list[int]] = []

        nums.sort()

        idx = 0

        while idx < len(nums):
            if nums[idx + 2] - nums[idx] > k:
                return []

            out.append(nums[idx : idx + 3])
            idx += 3

        return out
