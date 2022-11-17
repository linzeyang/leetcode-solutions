"""1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        return self._find_a_val(cloned, target.val)

    def _find_a_val(self, node: TreeNode | None, val) -> TreeNode | None:
        if node is None:
            return

        if node.val == val:
            return node

        return self._find_a_val(node.left, val) or self._find_a_val(node.right, val)
