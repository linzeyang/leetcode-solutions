"""2460. Apply Operations to an Array"""

from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        part1 = [num for num in nums if num > 0]
        part2 = (len(nums) - len(part1)) * [0]

        return part1 + part2
