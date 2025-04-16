"""2760. Longest Even Odd Subarray With Threshold"""

from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        out = idx = 0

        while idx < len(nums):
            if nums[idx] & 1 or nums[idx] > threshold:
                idx += 1
                continue

            jdx = idx + 1

            while jdx < len(nums):
                if (nums[jdx] & 1 == nums[jdx - 1] & 1) or (nums[jdx] > threshold):
                    break

                jdx += 1

            out = max(out, jdx - idx)

            idx = jdx

        return out
