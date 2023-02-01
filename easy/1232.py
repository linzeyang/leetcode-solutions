"""1232. Check If It Is a Straight Line"""

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        vector = (
            coordinates[0][0] - coordinates[1][0],
            coordinates[0][1] - coordinates[1][1],
        )

        if vector[0] == 0:
            for coor in coordinates:
                if coor[0] != coordinates[0][0]:
                    return False

            return True

        if vector[1] == 0:
            for coor in coordinates:
                if coor[1] != coordinates[0][1]:
                    return False

            return True

        for idx in range(1, len(coordinates) - 1):
            point_a = coordinates[idx]
            point_b = coordinates[idx + 1]

            if (point_a[0] - point_b[0]) / (point_a[1] - point_b[1]) != vector[
                0
            ] / vector[1]:
                return False

        return True
