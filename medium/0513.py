"""513. Find Bottom Left Tree Value"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        level: list[TreeNode] = [root]

        while level:
            temp_level: list[TreeNode] = []

            for node in level:
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right)

            if not temp_level:
                break

            level = temp_level

        return level[0].val
