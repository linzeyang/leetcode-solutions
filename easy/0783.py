"""783. Minimum Distance Between BST Nodes"""

# This problem is the same as 530

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        traversed = self._traverse(root)

        out = 100_000

        for idx in range(1, len(traversed)):
            out = min(out, traversed[idx] - traversed[idx - 1])

        return out

    def _traverse(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        return self._traverse(root.left) + [root.val] + self._traverse(root.right)
