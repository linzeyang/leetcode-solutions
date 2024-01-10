"""872. Leaf-Similar Trees"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self._leaf_values(root1) == self._leaf_values(root2)

    def _leaf_values(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        return self._leaf_values(root.left) + self._leaf_values(root.right)
