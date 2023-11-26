"""2946. Matrix Similarity After Cyclic Shifts"""

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        height = len(mat)
        width = len(mat[0])

        if k % width == 0:
            return True

        temp: set[tuple[int, int]] = set()

        for idx in range(width):
            if idx % 2 == 0:
                target = (idx + k) % width
            else:
                target = (idx - k) % width

            if tuple(sorted((idx, target))) in temp:
                continue

            for jdx in range(height):
                if mat[jdx][idx] != mat[jdx][target]:
                    return False

            temp.add(tuple(sorted((idx, target))))

        return True
