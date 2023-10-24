"""2908. Minimum Sum of Mountain Triplets I"""

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        summ = 0

        for idx in range(len(nums) - 2):
            for jdx in range(idx + 1, len(nums) - 1):
                if nums[jdx] <= nums[idx]:
                    continue

                for kdx in range(jdx + 1, len(nums)):
                    if nums[kdx] >= nums[jdx]:
                        continue

                    sub_sum = nums[idx] + nums[jdx] + nums[kdx]

                    if not summ or sub_sum < summ:
                        summ = sub_sum

        return summ or -1
