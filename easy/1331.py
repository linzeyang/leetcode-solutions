"""1331. Rank Transform of an Array"""

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted: list[int] = sorted(arr)

        mapping: dict[int, int] = {}

        rank = 0

        for num in arr_sorted:
            if num not in mapping:
                rank += 1
                mapping[num] = rank

        return [mapping[number] for number in arr]
