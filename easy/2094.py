"""2094. Finding 3-Digit Even Numbers"""

from itertools import permutations
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        return sorted(
            {
                (a * 100 + b * 10 + c)
                for a, b, c in permutations(digits, 3)
                if a != 0 and c % 2 == 0
            }
        )
