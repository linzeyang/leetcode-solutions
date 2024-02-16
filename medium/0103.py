"""103. Binary Tree Zigzag Level Order Traversal"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        out: list[list[int]] = []
        direct = 1

        level = [root]

        while level:
            if direct > 0:
                out.append([node.val for node in level])
            else:
                out.append([node.val for node in level[::-1]])

            direct = -direct

            temp_level = []

            for node in level:
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right)

            level = temp_level

        return out
