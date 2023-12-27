"""47. Permutations II"""

from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ss = set()
        out = []

        for perm in permutations(nums, len(nums)):
            if perm not in ss:
                ss.add(perm)
                out.append(list(perm))

        return out


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        results: set[tuple[int, ...]] = set()

        self._backtrack(nums, [], results)

        return list(results)

    def _backtrack(
        self, nums: list[int], path: list[int], results: set[tuple[int, ...]]
    ):
        if len(path) == len(nums):
            results.add(tuple(nums[idx] for idx in path))
            return

        for idx in range(len(nums)):
            if idx not in path:
                path.append(idx)
                self._backtrack(nums, path, results)
                path.pop()
