"""3355. Zero Array Transformation I"""

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        length = len(nums)
        diffs: list[int] = [0] * (length + 1)

        # Build difference array for queries coverage
        for left, right in queries:
            diffs[left] += 1

            if right + 1 < length:
                diffs[right + 1] -= 1

        # Prefix sum to get coverage count
        for idx in range(1, length):
            diffs[idx] += diffs[idx - 1]

        # Check if coverage is enough to decrement nums to zero
        for idx in range(length):
            if diffs[idx] < nums[idx]:
                return False

        return True
