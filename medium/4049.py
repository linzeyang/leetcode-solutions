"""
4049. Count Values With Equally Spaced Occurrences II

https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-ii/

Biweekly Contest 191
"""


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        mapping: dict[int, list[int]] = {}

        for idx, num in enumerate(nums):
            mapping.setdefault(num, []).append(idx)

        out: int = 0

        for idxs in mapping.values():
            if len(idxs) < 3:
                continue

            common_diff: int = idxs[0] - idxs[1]

            for jdx in range(1, len(idxs) - 1):
                if idxs[jdx] - idxs[jdx + 1] != common_diff:
                    break
            else:
                out += 1

        return out
