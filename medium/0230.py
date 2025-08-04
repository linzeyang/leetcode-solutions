"""230. Kth Smallest Element in a BST"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        all_vals: list[int] = self._traverse(root)

        return all_vals[k - 1]

    def _traverse(self, node: TreeNode | None) -> list[int]:
        if not node:
            return []

        return self._traverse(node.left) + [node.val] + self._traverse(node.right)
