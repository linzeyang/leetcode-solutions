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
        # Runtime beats 30.81%
        # Memory beats 83.94%
        if root is None:
            return []

        out = []
        next_level = [root]

        while next_level:
            new_next_level = []
            sub_out = []

            for node in next_level:
                sub_out.append(node.val)
                if node.left is not None:
                    new_next_level.append(node.left)
                if node.right is not None:
                    new_next_level.append(node.right)

            out.append(sub_out)
            next_level = new_next_level

        return out
