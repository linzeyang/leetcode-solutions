"""3364. Minimum Positive Sum Subarray"""

from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:  # noqa: E741
        length = len(nums)

        candidates: list[int] = []

        for idx in range(length - l + 1):
            sub_sum = sum(nums[idx : idx + l])

            if sub_sum > 0:
                candidates.append(sub_sum)

            for jdx in range(idx + l, min(length, idx + r)):
                sub_sum += nums[jdx]

                if sub_sum > 0:
                    candidates.append(sub_sum)

        return min(candidates) if candidates else -1
