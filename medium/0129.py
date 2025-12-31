"""129. Sum Root to Leaf Numbers"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum_root_to_leaf(node: TreeNode | None, base: int) -> int:
            if not node:
                return base // 10

            if not node.left:
                return sum_root_to_leaf(node.right, (base + node.val) * 10)

            if not node.right:
                return sum_root_to_leaf(node.left, (base + node.val) * 10)

            return sum_root_to_leaf(
                node.left, (base + node.val) * 10
            ) + sum_root_to_leaf(node.right, (base + node.val) * 10)

        return sum_root_to_leaf(root, base=0)
