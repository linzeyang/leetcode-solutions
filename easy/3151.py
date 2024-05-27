"""3151. Special Array I"""

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        parity = bool(nums[0] & 1)

        for idx in range(1, len(nums)):
            parity = not parity

            if nums[idx] & 1 != parity:
                return False

        return True
