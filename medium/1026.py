"""1026. Maximum Difference Between Node and Ancestor"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self._max_diff(root, ancestor_vals=[])

    def _max_diff(self, root, ancestor_vals: list[int]) -> int:
        out = max((abs(val - root.val) for val in ancestor_vals), default=0)

        if root.left:
            left_max = self._max_diff(root.left, ancestor_vals + [root.val])
            if left_max > out:
                out = left_max

        if root.right:
            right_max = self._max_diff(root.right, ancestor_vals + [root.val])
            if right_max > out:
                out = right_max

        return out
