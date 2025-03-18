"""3483. Unique 3-Digit Even Numbers"""

from itertools import permutations
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        candidates: set[tuple[int, int, int]] = set()

        for a, b, c in permutations(digits, 3):
            if c & 1 == 0 and a != 0:
                candidates.add((a, b, c))

        return len(candidates)
