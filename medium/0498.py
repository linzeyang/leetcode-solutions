"""498. Diagonal Traverse"""

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        out: list[int] = []

        m = len(mat)
        n = len(mat[0])

        k = m + n - 1

        ancher_x, ancher_y = 0, 0

        for _ in range(k):
            temp: list[int] = []

            x, y = ancher_x, ancher_y

            while x < n and y >= 0:
                temp.append(mat[y][x])
                x += 1
                y -= 1

            if _ % 2:
                out.extend(temp[::-1])
            else:
                out.extend(temp)

            if ancher_y < m - 1:
                ancher_y += 1
            else:
                ancher_x += 1

        return out
