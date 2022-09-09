"""
104. Maximum Depth of Binary Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Slow:
        # Runtime: 77 ms, faster than 27.11% of Python3 online submissions for Maximum Depth of Binary Tree.
        # Memory Usage: 16.4 MB, less than 23.59% of Python3 online submissions for Maximum Depth of Binary Tree.
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
