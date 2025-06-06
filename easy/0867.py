"""867. Transpose Matrix"""

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out: list[list[int]] = []

        for jdx in range(len(matrix[0])):
            out.append([row[jdx] for row in matrix])

        return out


# use numpy instead:
# import numpy as np

# class Solution:
#     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#         return np.array(matrix).T.tolist()
