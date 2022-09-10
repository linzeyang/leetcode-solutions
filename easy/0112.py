"""
112. Path Sum
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Very slow:
        # Runtime: 102 ms, faster than 5.42% of Python3 online submissions for Path Sum.
        # Memory Usage: 15.2 MB, less than 15.84% of Python3 online submissions for Path Sum.
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        new_target = targetSum - root.val

        return self.hasPathSum(root.left, new_target) or self.hasPathSum(
            root.right, new_target
        )
