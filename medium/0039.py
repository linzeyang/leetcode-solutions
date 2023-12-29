"""39. Combination Sum"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: list[list[int]] = []
        self._backtrack(candidates, 0, target, [], result)
        return result

    def _backtrack(
        self,
        candidates: list[int],
        start_idx: int,
        target: int,
        path: list[int],
        result: list[list[int]],
    ) -> None:
        if sum(path) == target:
            result.append(path[:])
            return

        if sum(path) > target:
            return

        for idx, num in enumerate(candidates[start_idx:]):
            path.append(num)
            self._backtrack(candidates, start_idx + idx, target, path, result)
            path.pop()
