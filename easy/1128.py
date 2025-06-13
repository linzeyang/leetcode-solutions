"""1128. Number of Equivalent Domino Pairs"""

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mapping: dict[tuple[int, int], int] = {}

        for a, b in dominoes:
            if (a, b) in mapping:
                mapping[(a, b)] += 1
            elif (b, a) in mapping:
                mapping[(b, a)] += 1
            else:
                mapping[(a, b)] = 1

        return sum(val * (val - 1) // 2 for val in mapping.values())
