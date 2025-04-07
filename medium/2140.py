"""2140. Solving Questions With Brainpower"""

from functools import lru_cache
from typing import List


class Solution:
    """Resursion with LRU cahce"""

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.questions = questions

        return self._solve(start_idx=0)

    @lru_cache(maxsize=10_000)
    def _solve(self, start_idx: int) -> int:
        length = len(self.questions)

        points, skip = self.questions[start_idx]

        if start_idx == length - 1:
            return points

        if start_idx + skip >= length - 1:
            return max(points, self._solve(start_idx=start_idx + 1))

        return max(
            points + self._solve(start_idx=start_idx + skip + 1),
            self._solve(start_idx=start_idx + 1),
        )


if __name__ == "__main__":
    testcases: tuple[tuple[tuple[list[list[int]]], int], ...] = (
        (([[3, 2], [4, 3], [4, 4], [2, 5]],), 5),
        (([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],), 7),
    )

    for case in testcases:
        assert Solution().mostPoints(*case[0]) == case[1]
