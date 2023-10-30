"""542. 01 Matrix"""

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        out: list[list[int]] = [[-1] * len(mat[0]) for _ in range(len(mat))]
        queue = deque()

        for idx, row in enumerate(mat):
            for jdx, node in enumerate(row):
                if node == 0:
                    out[idx][jdx] = 0
                    queue.append((idx, jdx))

        while queue:
            coordx, coordy = queue.popleft()

            if coordx > 0 and out[coordx - 1][coordy] == -1:
                queue.append((coordx - 1, coordy))
                out[coordx - 1][coordy] = out[coordx][coordy] + 1
            if coordx < len(mat) - 1 and out[coordx + 1][coordy] == -1:
                queue.append((coordx + 1, coordy))
                out[coordx + 1][coordy] = out[coordx][coordy] + 1
            if coordy > 0 and out[coordx][coordy - 1] == -1:
                queue.append((coordx, coordy - 1))
                out[coordx][coordy - 1] = out[coordx][coordy] + 1
            if coordy < len(mat[0]) - 1 and out[coordx][coordy + 1] == -1:
                queue.append((coordx, coordy + 1))
                out[coordx][coordy + 1] = out[coordx][coordy] + 1

        return out
