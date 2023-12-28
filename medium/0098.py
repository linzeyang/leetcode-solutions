"""98. Validate Binary Search Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self._is_valid(root, None, None)

    def _is_valid(
        self,
        root: Optional[TreeNode],
        left_bound: Optional[int],
        right_bound: Optional[int],
    ) -> bool:
        if not root:
            return True

        if left_bound is not None and root.val <= left_bound:
            return False

        if right_bound is not None and root.val >= right_bound:
            return False

        if not root.left and not root.right:
            return True

        return self._is_valid(
            root.left, left_bound=left_bound, right_bound=root.val
        ) and self._is_valid(root.right, left_bound=root.val, right_bound=right_bound)
