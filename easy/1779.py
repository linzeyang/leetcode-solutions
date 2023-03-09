"""1779. Find Nearest Point That Has the Same X or Y Coordinate"""

from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        temp = {}

        for idx, point in enumerate(points):
            if x != point[0] and y != point[1]:
                continue

            m_dis = abs(x - point[0]) + abs(y - point[1])

            if m_dis not in temp:
                temp[m_dis] = [idx]
            else:
                temp[m_dis].append(idx)

        if not temp:
            return -1

        min_m_dis = min(temp.keys())

        return min(temp[min_m_dis])
