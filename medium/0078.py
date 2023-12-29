"""78. Subsets"""

from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]

        for i in range(1, len(nums) + 1):
            out.extend([list(combo) for combo in combinations(nums, i)])

        return out


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out: list[list[int]] = [[]]

        for idx in range(1, len(nums) + 1):
            out.extend(self._subsets(length=idx, nums=nums))

        return out

    def _subsets(self, length: int, nums: list[int]) -> list[list[int]]:
        results: list[list[int]] = []
        self._backtrack(nums=nums, length=length, start_idx=0, path=[], results=results)
        return results

    def _backtrack(
        self,
        nums: list[int],
        length: int,
        start_idx: int,
        path: list[int],
        results: list[list[int]],
    ) -> None:
        if len(path) == length:
            results.append(path[:])
            return

        for num in nums[start_idx:]:
            if num not in path:
                path.append(num)
                self._backtrack(
                    nums=nums,
                    length=length,
                    start_idx=nums.index(num) + 1,
                    path=path,
                    results=results,
                )
                path.pop()
