"""700. Search in a Binary Search Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return

        node = root

        while node is not None:
            if val == node.val:
                return node
            if val < node.val:
                node = node.left
            else:
                node = node.right
