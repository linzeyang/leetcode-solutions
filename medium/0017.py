"""17. Letter Combinations of a Phone Number"""

from itertools import product
from typing import List

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


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        lis = [MAPPING[d] for d in digits]

        return ["".join(pro) for pro in product(*lis)]


CHARS = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result: list[str] = []
        self._backtrack(digits, 0, [], result)
        return result

    def _backtrack(
        self, digits: str, idx: int, path: list[str], result: list[str]
    ) -> None:
        if len(path) == len(digits):
            result.append("".join(path))
            return

        for char in CHARS[int(digits[idx]) - 2]:
            path.append(char)
            self._backtrack(digits, idx + 1, path, result)
            path.pop()
