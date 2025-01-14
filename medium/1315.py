"""1315. Sum of Nodes with Even-Valued Grandparent"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        out = 0

        if root.val % 2 == 0:
            out += self._sum_children(root.left) + self._sum_children(root.right)

        out += self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)

        return out

    def _sum_children(self, root) -> int:
        if not root:
            return 0

        return (root.left.val if root.left else 0) + (
            root.right.val if root.right else 0
        )
