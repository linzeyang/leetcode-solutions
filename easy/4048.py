"""
4048. Count Values With Equally Spaced Occurrences I

https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-i/

Biweekly Contest 191
"""


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        mapping: dict[int, list[int]] = {}

        for idx, num in enumerate(nums):
            mapping.setdefault(num, []).append(idx)

        out: int = 0

        for idxs in mapping.values():
            if len(idxs) != 3:
                continue

            if idxs[0] - idxs[1] == idxs[1] - idxs[2]:
                out += 1

        return out
