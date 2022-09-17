"""
404. Sum of Left Leaves
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Very slow:
        # Runtime: 70 ms, faster than 12.03% of Python3 online submissions for Sum of Left Leaves.
        # Memory Usage: 14.8 MB, less than 45.70% of Python3 online submissions for Sum of Left Leaves.
        if root is None:
            return 0

        return sub_tree(root.left, is_left=1) + sub_tree(root.right, is_left=0)


def sub_tree(node: Optional[TreeNode], is_left: bool) -> int:
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return node.val if is_left else 0

    return sub_tree(node.left, is_left=1) + sub_tree(node.right, is_left=0)
