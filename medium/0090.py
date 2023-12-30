"""90. Subsets II"""

from itertools import combinations
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums) + 1):
            ss = set()
            for comb in combinations(nums, i):
                if comb not in ss:
                    ss.add(comb)
                    out.append(list(comb))

        return out


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out: list[list[int]] = [[]]

        for idx in range(1, len(nums) + 1):
            out.extend(self._subsets(idx, nums))

        return out

    def _subsets(self, length: int, nums: list[int]) -> set[tuple[int, ...]]:
        result: set[tuple[int, ...]] = set()
        self._backtrack(nums, length, 0, [], result)
        return result

    def _backtrack(
        self,
        nums: list[int],
        length: int,
        start_idx: int,
        path: list[int],
        result: set[tuple[int, ...]],
    ) -> None:
        if len(path) == length:
            result.add(tuple(path[:]))
            return

        for idx, num in enumerate(nums[start_idx:]):
            path.append(num)
            self._backtrack(nums, length, start_idx + idx + 1, path, result)
            path.pop()
