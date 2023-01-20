"""896. Monotonic Array"""

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        length = len(nums)

        if length < 3:
            return True

        flag = 0

        for idx in range(1, length):
            if nums[idx] == nums[idx - 1]:
                continue

            if flag == 0:
                if nums[idx] > nums[idx - 1]:
                    flag = 1
                else:
                    flag = -1
            elif flag == 1 and nums[idx] < nums[idx - 1]:
                return False
            elif flag == -1 and nums[idx] > nums[idx - 1]:
                return False

        return True
