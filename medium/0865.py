"""865. Smallest Subtree with all the Deepest Nodes"""

# This question is the same as 1123

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        _, lca = self._get_tree_level_and_lca(node=root)

        return lca

    def _get_tree_level_and_lca(
        self, node: TreeNode | None
    ) -> tuple[int, TreeNode | None]:
        """Recursively get level and the Lowest Common Ancestor of given tree node"""

        if not node:
            return 0, None

        left_level, left_lca = self._get_tree_level_and_lca(node.left)
        right_level, right_lca = self._get_tree_level_and_lca(node.right)

        if left_level == right_level:
            return left_level + 1, node

        if left_level > right_level:
            return left_level + 1, left_lca

        return right_level + 1, right_lca
