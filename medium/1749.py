"""1749. Maximum Absolute Sum of Any Subarray"""

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxx = []

        current_max = sum_so_far = nums[0]

        for idx in range(1, len(nums)):
            sum_so_far += nums[idx]
            current_max = max(current_max, sum_so_far)

        maxx.append(current_max)

        for idx in range(1, len(nums)):
            maxx.append(maxx[-1] - nums[idx - 1])

        max_possible = max(maxx)

        minn = []

        current_min = sum_so_far = nums[0]

        for idx in range(1, len(nums)):
            sum_so_far += nums[idx]
            current_min = min(current_min, sum_so_far)

        minn.append(current_min)

        for idx in range(1, len(nums)):
            minn.append(minn[-1] - nums[idx - 1])

        min_possible = min(minn)

        return max(abs(max_possible), abs(min_possible))
