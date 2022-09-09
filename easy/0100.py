"""
100. Same Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Fast:
        # Runtime: 35 ms, faster than 86.37% of Python3 online submissions for Same Tree.
        # Memory Usage: 14 MB, less than 29.23% of Python3 online submissions for Same Tree.
        if p is None and q is None:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p=p.left, q=q.left) and self.isSameTree(
            p=p.right, q=q.right
        )
