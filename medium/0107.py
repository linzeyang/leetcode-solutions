"""107. Binary Tree Level Order Traversal II"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        out: list[list[int]] = [[root.val]]

        level = []

        if root.left:
            level.append(root.left)
        if root.right:
            level.append(root.right)

        while level:
            out.append([node.val for node in level])

            temp_level = []

            for node in level:
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right)

            level = temp_level

        return out[::-1]
