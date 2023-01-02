"""637. Average of Levels in Binary Tree"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        temp = [root]
        out = [float(root.val)]

        while temp:
            nodes = []

            for node in temp:
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)

            if not nodes:
                break

            out.append(sum(node.val for node in nodes) / len(nodes))
            temp = nodes

        return out
