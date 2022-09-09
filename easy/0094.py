"""
94. Binary Tree Inorder Traversal
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Fast:
        # Runtime: 30 ms, faster than 95.21% of Python3 online submissions for Binary Tree Inorder Traversal.
        # Memory Usage: 13.8 MB, less than 96.73% of Python3 online submissions for Binary Tree Inorder Traversal.
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )
