"""3577. Count the Number of Computer Unlocking Permutations"""

from math import perm
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        length = len(complexity)

        for idx in range(1, length):
            if complexity[idx] <= complexity[0]:
                return 0

        return perm(length - 1, length - 1) % (1_000_000_000 + 7)
