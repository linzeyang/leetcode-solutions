"""114. Flatten Binary Tree to Linked List"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Runtime: 57 ms, faster than 61.27% of Python3 online submissions for Flatten Binary Tree to Linked List.
        # Memory Usage: 15.3 MB, less than 46.97% of Python3 online submissions for Flatten Binary Tree to Linked List.
        if root is None:
            return

        if root.left is None:
            self.flatten(root.right)
            return

        self.flatten(root.left)
        self.flatten(root.right)

        node = root.left

        while node.right is not None:
            node = node.right

        node.right = root.right
        root.right = root.left
        root.left = None
