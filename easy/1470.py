"""1470. Shuffle the Array"""

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        half = len(nums) // 2

        for i in range(half):
            out.append(nums[i])
            out.append(nums[i + half])

        return out
