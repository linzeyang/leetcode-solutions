"""106. Construct Binary Tree from Inorder and Postorder Traversal"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return

        root = TreeNode(val=postorder[-1])

        if len(postorder) == 1:
            return root

        root_idx = inorder.index(postorder[-1])

        root.left = self.buildTree(
            inorder=inorder[:root_idx], postorder=postorder[:root_idx]
        )
        root.right = self.buildTree(
            inorder=inorder[root_idx + 1 :], postorder=postorder[root_idx:-1]
        )

        return root
