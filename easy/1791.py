"""1791. Find Center of Star Graph"""

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()
