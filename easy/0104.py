"""104. Maximum Depth of Binary Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        out = 1
        next_level: list[TreeNode] = []

        if root.left:
            next_level.append(root.left)
        if root.right:
            next_level.append(root.right)

        while next_level:
            out += 1
            temp: list[TreeNode] = []

            for node in next_level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            next_level = temp

        return out
