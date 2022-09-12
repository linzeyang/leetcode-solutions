"""
145. Binary Tree Postorder Traversal
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Very slow:
        # Runtime: 67 ms, faster than 6.95% of Python3 online submissions for Binary Tree Postorder Traversal.
        # Memory Usage: 13.8 MB, less than 96.76% of Python3 online submissions for Binary Tree Postorder Traversal.
        if root is None:
            return []

        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )
