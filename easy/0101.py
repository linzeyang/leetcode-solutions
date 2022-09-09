"""
101. Symmetric Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Very slow:
        # Runtime: 68 ms, faster than 17.96% of Python3 online submissions for Symmetric Tree.
        # Memory Usage: 13.9 MB, less than 60.59% of Python3 online submissions for Symmetric Tree.
        if root is None:
            return True

        return check_symmetric(root.left, root.right)


def check_symmetric(nodea: Optional[TreeNode], nodeb: Optional[TreeNode]) -> bool:
    if nodea is None and nodeb is None:
        return True

    if nodea is None or nodeb is None or nodea.val != nodeb.val:
        return False

    return check_symmetric(nodea.left, nodeb.right) and check_symmetric(
        nodea.right, nodeb.left
    )
