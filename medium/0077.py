"""77. Combinations"""

from itertools import combinations
from typing import List


# Using `itertools.combinations`
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Runtime: 139 ms, faster than 89.09% of Python3 online submissions for Combinations.
        # Memory Usage: 15.8 MB, less than 95.97% of Python3 online submissions for Combinations.
        return [list(comb) for comb in combinations(range(1, n + 1), k)]
