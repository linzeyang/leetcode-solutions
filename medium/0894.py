"""894. All Possible Full Binary Trees"""

from functools import lru_cache
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self._possibles(n)

    @lru_cache(maxsize=10)
    def _possibles(self, n: int) -> list[TreeNode]:
        if n == 1:
            return [TreeNode()]

        if n == 3:
            return [TreeNode(left=TreeNode(), right=TreeNode())]

        out: list[TreeNode] = []

        for num in range(1, n - 1, 2):
            for possi_left in self._possibles(n=num):
                for possi_right in self._possibles(n=n - 1 - num):
                    out.append(TreeNode(left=possi_left, right=possi_right))

        return out
