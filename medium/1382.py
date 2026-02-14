"""1382. Balance a Binary Search Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/balance-a-binary-search-tree/
    Weekly Contest 180
    """

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values: list[int] = []
        self._inorder_traversal(root=root, values=values)

        return self._build_tree(values=values, left=0, right=len(values) - 1)

    def _inorder_traversal(self, root: TreeNode | None, values: list[int]) -> None:
        if not root:
            return

        self._inorder_traversal(root=root.left, values=values)
        values.append(root.val)
        self._inorder_traversal(root=root.right, values=values)

    def _build_tree(self, values: list[int], left: int, right: int) -> TreeNode | None:
        if left > right:
            return

        mid: int = (left + right) // 2
        root = TreeNode(val=values[mid])
        root.left = self._build_tree(values=values, left=left, right=mid - 1)
        root.right = self._build_tree(values=values, left=mid + 1, right=right)

        return root
