"""1382. Balance a Binary Search Tree"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        array = self._construct_array(root)

        return self._construct_tree(array)

    def _construct_array(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        return (
            self._construct_array(root.left)
            + [root.val]
            + self._construct_array(root.right)
        )

    def _construct_tree(self, array: list[int]) -> TreeNode | None:
        if not array:
            return

        mid = len(array) // 2

        return TreeNode(
            val=array[mid],
            left=self._construct_tree(array[:mid]),
            right=self._construct_tree(array[mid + 1 :]),
        )
