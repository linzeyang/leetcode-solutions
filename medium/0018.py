"""18. 4Sum"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out: set[tuple[int, int, int, int]] = set()

        nums.sort()

        for idx in range(len(nums) - 3):
            targ = target - nums[idx]

            for jdx in range(idx + 1, len(nums) - 2):
                targ2 = targ - nums[jdx]

                left, right = jdx + 1, len(nums) - 1

                while left < right:
                    if nums[left] + nums[right] == targ2:
                        out.add((nums[idx], nums[jdx], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < targ2:
                        left += 1
                    else:
                        right -= 1

        return [list(tup) for tup in out]
