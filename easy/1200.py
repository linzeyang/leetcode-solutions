"""1200. Minimum Absolute Difference"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-absolute-difference/
    Weekly Contest 155
    """

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        out: list[list[int]] = []

        arr.sort()

        min_diff: int | float = float("inf")

        for idx in range(len(arr) - 1):
            diff: int = arr[idx + 1] - arr[idx]

            if diff < min_diff:
                min_diff = diff
                out = [[arr[idx], arr[idx + 1]]]
            elif diff == min_diff:
                out.append([arr[idx], arr[idx + 1]])

        return out
