"""700. Search in a Binary Search Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return

        node = root

        while node is not None:
            if val == node.val:
                return node
            if val < node.val:
                node = node.left
            else:
                node = node.right


class Solution2:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)

        return self.searchBST(root.left, val)
