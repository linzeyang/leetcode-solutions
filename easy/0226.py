"""
226. Invert Binary Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Very slow:
        # Runtime: 83 ms, faster than 5.59% of Python3 online submissions for Invert Binary Tree.
        # Memory Usage: 13.9 MB, less than 56.99% of Python3 online submissions for Invert Binary Tree.
        if root is None:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
