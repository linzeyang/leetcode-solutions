"""
3898. Find the Degree of Each Vertex

https://leetcode.com/problems/find-the-degree-of-each-vertex/

Weekly Contest 497
"""


class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in matrix]
