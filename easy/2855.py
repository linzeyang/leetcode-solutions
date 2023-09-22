"""2855. Minimum Right Shifts to Sort the Array"""

from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        downgrade = 0
        downgrade_idx = -1

        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                downgrade += 1
                downgrade_idx = idx

        if not downgrade:
            return 0

        if downgrade > 1 or nums[0] < nums[-1]:
            return -1

        return len(nums) - downgrade_idx - 1
