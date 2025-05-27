"""653. Two Sum IV - Input is a BST"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums: list[int] = self._traverse(root)
        mapping: dict[int, int] = {}

        for idx, num in enumerate(nums):
            if (k - num) in mapping:
                return True

            mapping[num] = idx

        return False

    def _traverse(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        return self._traverse(root.left) + [root.val] + self._traverse(root.right)
