"""
1886. Determine Whether Matrix Can Be Obtained By Rotation

https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

Weekly Contest 244
"""


class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True

            mat: list[list[int]] = [list(row) for row in zip(*mat[::-1], strict=True)]

        return False
