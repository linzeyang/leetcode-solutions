"""986. Interval List Intersections"""

from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        out: list[list[int]] = []

        if firstList[-1][-1] < secondList[0][0]:
            return []

        for start1, end1 in firstList:
            if start1 > secondList[-1][-1]:
                break

            for start2, end2 in secondList:
                if start1 > end2:
                    continue

                if end1 < start2:
                    break

                out.append([max(start1, start2), min(end1, end2)])

        return out
