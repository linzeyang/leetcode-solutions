"""965. Univalued Binary Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self._is_univalue(root.left, root.val) and self._is_univalue(
            root.right, root.val
        )

    def _is_univalue(self, root: TreeNode | None, val: int) -> bool:
        if root is None:
            return True

        if root.val != val:
            return False

        return self._is_univalue(root.left, val) and self._is_univalue(root.right, val)
