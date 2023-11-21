"""112. Path Sum"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        new_target = targetSum - root.val

        return self.hasPathSum(root.left, new_target) or self.hasPathSum(
            root.right, new_target
        )
