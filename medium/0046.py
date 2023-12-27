"""46. Permutations"""

from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(perm) for perm in permutations(nums, len(nums))]


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        results: list[list[int]] = []

        self._backtrack(nums, [], results)

        return results

    def _backtrack(self, nums: list[int], path: list[int], results: list[list[int]]):
        if len(path) == len(nums):
            results.append(path[:])
            return

        for num in nums:
            if num not in path:
                path.append(num)
                self._backtrack(nums, path, results)
                path.pop()
