"""2012. Sum of Beauty in the Array"""

from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        maxs: list[int] = [nums[0]]

        for idx in range(1, len(nums)):
            maxs.append(max(maxs[-1], nums[idx]))

        mins: list[int] = [nums[-1]]

        for idx in range(2, len(nums) + 1):
            mins.append(min(mins[-1], nums[-idx]))

        mins.reverse()

        out = 0

        for idx in range(1, len(nums) - 1):
            if maxs[idx - 1] < nums[idx] < mins[idx + 1]:
                out += 2
            elif nums[idx - 1] < nums[idx] < nums[idx + 1]:
                out += 1

        return out
