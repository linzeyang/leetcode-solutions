"""102. Binary Tree Level Order Traversal"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        out: list[list[int]] = [[root.val]]
        next_level: list[TreeNode] = []

        if root.left:
            next_level.append(root.left)
        if root.right:
            next_level.append(root.right)

        while next_level:
            out.append([node.val for node in next_level])
            temp_next_level: list[TreeNode] = []

            for node in next_level:
                if node.left:
                    temp_next_level.append(node.left)
                if node.right:
                    temp_next_level.append(node.right)

            next_level = temp_next_level

        return out
