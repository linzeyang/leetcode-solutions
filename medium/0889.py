"""889. Construct Binary Tree from Preorder and Postorder Traversal"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return

        root = TreeNode(val=preorder[0])

        if len(preorder) == 1:
            return root

        _preorder = set()
        _postorder = set()

        for idx in range(1, len(preorder)):
            _preorder.add(preorder[idx])
            _postorder.add(postorder[idx - 1])

            if _preorder == _postorder:
                break

        root.left = self.constructFromPrePost(
            preorder=preorder[1 : idx + 1], postorder=postorder[:idx]
        )
        root.right = self.constructFromPrePost(
            preorder=preorder[idx + 1 :], postorder=postorder[idx:]
        )

        return root
