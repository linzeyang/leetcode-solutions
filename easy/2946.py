"""
2946. Matrix Similarity After Cyclic Shifts

https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

Weekly Contest 373
"""

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        width: int = len(mat[0])

        even_shift: int = width - k % width
        odd_shift: int = k % width

        for idx, row in enumerate(mat):
            if idx & 1 == 0:
                for jdx in range(even_shift):
                    if row[jdx] != row[(jdx + even_shift) % width]:
                        return False
            else:
                for jdx in range(odd_shift):
                    if row[jdx] != row[(jdx + odd_shift) % width]:
                        return False

        return True
