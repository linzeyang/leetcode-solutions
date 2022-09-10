"""
111. Minimum Depth of Binary Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Very slow:
        # Runtime: 1301 ms, faster than 5.92% of Python3 online submissions for Minimum Depth of Binary Tree.
        # Memory Usage: 54.6 MB, less than 43.42% of Python3 online submissions for Minimum Depth of Binary Tree.
        if root is None:
            return 0

        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
