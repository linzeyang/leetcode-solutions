"""905. Sort Array By Parity"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = len(nums)

        for i in range(length - 1):
            if nums[i] % 2 == 0:
                continue

            for j in range(i + 1, length):
                if nums[j] % 2 == 1:
                    continue

                nums[i], nums[j] = nums[j], nums[i]
                break

        return nums
