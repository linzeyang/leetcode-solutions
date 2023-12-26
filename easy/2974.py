"""2974. Minimum Number Game"""

from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()

        out: list[int] = []

        for idx in range(0, len(nums), 2):
            out.append(nums[idx + 1])
            out.append(nums[idx])

        return out
