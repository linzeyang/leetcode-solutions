"""1008. Construct Binary Search Tree from Preorder Traversal"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return

        root = TreeNode(val=preorder[0])

        for idx, num in enumerate(preorder):
            if num > root.val:
                root.left = self.bstFromPreorder(preorder[1:idx])
                root.right = self.bstFromPreorder(preorder[idx:])
                break
        else:
            root.left = self.bstFromPreorder(preorder[1:])

        return root
