"""938. Range Sum of BST"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        if low == root.val == high:
            return root.val

        if low == root.val:
            return low + self.rangeSumBST(root.right, low=low, high=high)

        if high == root.val:
            return high + self.rangeSumBST(root.left, low=low, high=high)

        if low > root.val:
            return self.rangeSumBST(root.right, low=low, high=high)

        if high < root.val:
            return self.rangeSumBST(root.left, low=low, high=high)

        return (
            self.rangeSumBST(root.left, low=low, high=root.val)
            + self.rangeSumBST(root.right, low=root.val, high=high)
            + root.val
        )
