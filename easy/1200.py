"""1200. Minimum Absolute Difference"""

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        out = []
        diff = None

        ll = sorted(arr)

        for i in range(1, len(arr)):
            if diff is None:
                diff = ll[i] - ll[i - 1]
                out.append([ll[i - 1], ll[i]])
            elif (dif := ll[i] - ll[i - 1]) < diff:
                diff = dif
                out = [[ll[i - 1], ll[i]]]
            elif dif == diff:
                out.append([ll[i - 1], ll[i]])

        return out
