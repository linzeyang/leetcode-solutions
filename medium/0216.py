"""216. Combination Sum III"""

from itertools import combinations
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(comb) for comb in combinations(range(1, 10), k) if sum(comb) == n]


class Solution2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results: list[list[int]] = []

        self._backtrack([], 1, k, n, results)

        return results

    def _backtrack(
        self, path: list, init: int, k: int, n: int, results: list
    ) -> bool | None:
        if len(path) == k:
            if sum(path) == n:
                results.append(path[:])
                return True

            if sum(path) > n:
                return True

            return False

        for digit in range(init, 10):
            path.append(digit)

            res = self._backtrack(path, digit + 1, k, n, results)

            path.pop()

            if res:
                break
