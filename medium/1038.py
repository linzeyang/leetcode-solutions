"""1038. Binary Search Tree to Greater Sum Tree"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        lis: list[TreeNode] = self._inorder(root)

        accumulate = 0

        for idx in range(1, len(lis) + 1):
            lis[-idx].val += accumulate
            accumulate = lis[-idx].val

        return root

    def _inorder(self, root: TreeNode | None) -> list[TreeNode]:
        if not root:
            return []

        return self._inorder(root.left) + [root] + self._inorder(root.right)
