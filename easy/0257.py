"""257. Binary Tree Paths"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        return [f"{root.val}->{path}" for path in self.binaryTreePaths(root.left)] + [
            f"{root.val}->{path}" for path in self.binaryTreePaths(root.right)
        ]
