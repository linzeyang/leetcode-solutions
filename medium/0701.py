"""701. Insert into a Binary Search Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        if root.val < val:
            if not root.right:
                root.right = TreeNode(val=val)
            else:
                self.insertIntoBST(root.right, val)
        else:
            if not root.left:
                root.left = TreeNode(val=val)
            else:
                self.insertIntoBST(root.left, val)

        return root
