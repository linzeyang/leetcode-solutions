"""
144. Binary Tree Preorder Traversal
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Very slow:
        # Runtime: 62 ms, faster than 14.78% of Python3 online submissions for Binary Tree Preorder Traversal.
        # Memory Usage: 13.9 MB, less than 60.09% of Python3 online submissions for Binary Tree Preorder Traversal.
        if root is None:
            return []

        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
        )
