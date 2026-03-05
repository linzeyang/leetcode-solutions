"""3852. Smallest Pair With Different Frequencies"""

from collections import Counter


class Solution:
    """
    https://leetcode.com/problems/smallest-pair-with-different-frequencies/
    Biweekly Contest 177
    """

    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counter: Counter[int] = Counter(nums)

        if len(counter) < 2:
            return [-1, -1]

        sorted_keys: list[int] = sorted(counter.keys())

        x: int = sorted_keys[0]

        for idx in range(1, len(sorted_keys)):
            if counter[sorted_keys[idx]] != counter[x]:
                return [x, sorted_keys[idx]]

        return [-1, -1]
