"""1619. Mean of Array After Removing Some Elements"""

from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        length_five_percent = len(arr) // 20

        target = sorted(arr)[length_five_percent:-length_five_percent]

        return sum(target) / len(target)
