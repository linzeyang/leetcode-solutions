"""897. Increasing Order Search Tree"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        left_tree_head, left_tree_tail = self._do_branch(root.left)
        right_tree_head, _ = self._do_branch(root.right)

        if left_tree_tail is not None:
            left_tree_tail.right = root
        else:
            left_tree_head = root

        root.left = None
        root.right = right_tree_head

        return left_tree_head

    def _do_branch(
        self, root: TreeNode | None
    ) -> tuple[TreeNode | None, TreeNode | None]:
        if root is None:
            return None, None

        if root.left is None and root.right is None:
            return root, root

        if root.right is None:
            left_tree_head, left_tree_tail = self._do_branch(root.left)

            left_tree_tail.right = root
            root.left = None

            return left_tree_head, root

        if root.left is None:
            right_tree_head, right_tree_tail = self._do_branch(root.right)

            root.right = right_tree_head

            return root, right_tree_tail

        left_tree_head, left_tree_tail = self._do_branch(root.left)
        right_tree_head, right_tree_tail = self._do_branch(root.right)

        left_tree_tail.right = root
        root.left = None
        root.right = right_tree_head

        return left_tree_head, right_tree_tail
