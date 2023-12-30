"""105. Construct Binary Tree from Preorder and Inorder Traversal"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return

        root = TreeNode(val=preorder[0])

        if len(preorder) == 1:
            return root

        root_idx = inorder.index(preorder[0])

        root.left = self.buildTree(
            preorder=preorder[1 : 1 + root_idx], inorder=inorder[:root_idx]
        )
        root.right = self.buildTree(
            preorder=preorder[root_idx + 1 :], inorder=inorder[root_idx + 1 :]
        )

        return root
