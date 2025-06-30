"""2099. Find Subsequence of Length K With the Largest Sum"""

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        lis: list[tuple[int, int]] = sorted(
            ((idx, num) for idx, num in enumerate(nums)), key=lambda tup: tup[1]
        )

        out: list[int] = [tup[1] for tup in sorted(lis[-k:], key=lambda tup: tup[0])]

        return out
