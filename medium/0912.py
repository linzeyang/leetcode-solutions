"""912. Sort an Array"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # shell sort
        step = len(nums) // 2

        while step >= 1:
            for _ in range(step):
                self._sort(nums, list(range(_, len(nums), step)))

            step //= 2

        return nums

    @staticmethod
    def _sort(nums: list[int], indices: list[int]) -> None:
        if len(indices) == 1:
            return

        # inserting sort
        for jdx in range(1, len(indices)):
            for kdx in range(jdx - 1, -1, -1):
                if nums[indices[kdx]] > nums[indices[kdx + 1]]:
                    nums[indices[kdx]], nums[indices[kdx + 1]] = (
                        nums[indices[kdx + 1]],
                        nums[indices[kdx]],
                    )
                else:
                    break
