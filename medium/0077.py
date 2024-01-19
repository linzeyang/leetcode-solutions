"""77. Combinations"""

from itertools import combinations
from typing import List


# Using `itertools.combinations`
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(comb) for comb in combinations(range(1, n + 1), k)]
