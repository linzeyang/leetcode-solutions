"""15. 3Sum"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        out: set[tuple[int, int, int]] = set()

        for idx in range(len(nums) - 2):
            target = -nums[idx]

            jdx, kdx = idx + 1, len(nums) - 1

            while jdx < kdx:
                if nums[jdx] + nums[kdx] < target:
                    jdx += 1
                elif nums[jdx] + nums[kdx] > target:
                    kdx -= 1
                else:
                    out.add((nums[idx], nums[jdx], nums[kdx]))
                    jdx += 1
                    kdx -= 1

        return [list(tup) for tup in out]
