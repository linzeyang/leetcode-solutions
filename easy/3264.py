"""3264. Final Array State After K Multiplication Operations I"""

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            minn = -1
            minn_idx = -1

            for idx, num in enumerate(nums):
                if minn < 0 or num < minn:
                    minn = num
                    minn_idx = idx

            nums[minn_idx] = minn * multiplier

        return nums
