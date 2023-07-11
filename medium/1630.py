"""1630. Arithmetic Subarrays"""

from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        return [self._check(nums[low: high + 1]) for low, high in zip(l, r)]

    def _check(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return True

        nums.sort()

        diff = nums[0] - nums[1]

        for idx in range(1, len(nums) - 1):
            if nums[idx] - nums[idx + 1] != diff:
                return False

        return True
