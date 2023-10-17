"""1557. Minimum Number of Vertices to Reach All Nodes"""

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - {end for _, end in edges})
