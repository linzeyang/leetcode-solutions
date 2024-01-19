"""110. Balanced Binary Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left_result, left_diff = check_balanced(root.left)

        if not left_result:
            return False

        right_result, right_diff = check_balanced(root.right)

        if not right_result:
            return False

        return abs(left_diff - right_diff) < 2


def check_balanced(node: Optional[TreeNode]) -> tuple[bool, int]:
    if node is None:
        return True, 0

    if node.left is None and node.right is None:
        return True, 1

    left_result, left_diff = check_balanced(node.left)

    if not left_result:
        return False, 2

    right_result, right_diff = check_balanced(node.right)

    if not right_result:
        return False, 2

    if abs(left_diff - right_diff) >= 2:
        return False, 2

    return True, max(left_diff, right_diff) + 1
