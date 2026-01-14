"""1161. Maximum Level Sum of a Binary Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        out: int = 1
        max_sum: float = float("-inf")

        level: int = 0
        level_nodes: list = [root]

        while level_nodes:
            level += 1

            if (level_sum := sum(node.val for node in level_nodes)) > max_sum:
                max_sum = level_sum
                out = level

            next_level_nodes: list = []

            for node in level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            level_nodes = next_level_nodes

        return out
