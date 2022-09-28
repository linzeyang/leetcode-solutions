"""17. Letter Combinations of a Phone Number"""

from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Runtime: 62 ms, faster than 20.87% of Python3 online submissions for Letter Combinations of a Phone Number.
        # Memory Usage: 13.8 MB, less than 98.63% of Python3 online submissions for Letter Combinations of a Phone Number.
        if not digits:
            return []

        lis = [MAPPING[d] for d in digits]

        return ["".join(pro) for pro in product(*lis)]


MAPPING = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
