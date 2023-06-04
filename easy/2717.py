"""2717. Semi-Ordered Permutation"""

from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        length = len(nums)

        if nums[0] == 1 and nums[-1] == length:
            return 0

        n_before_one = False

        idx_one = idx_n = None

        for idx, num in enumerate(nums):
            if idx_one is not None and idx_n is not None:
                break

            if num == length:
                idx_n = idx

                if idx_one is None:
                    n_before_one = True
                else:
                    break

            elif num == 1:
                idx_one = idx

        return (
            idx_one + length - 1 - idx_n
            if not n_before_one
            else idx_one + length - 2 - idx_n
        )
