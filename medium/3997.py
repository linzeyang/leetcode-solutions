"""
3997. Count Dominant Nodes in a Binary Tree

https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

Weekly Contest 511
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:

        def _recursion(root: TreeNode | None) -> tuple[int, int]:
            """
            this function returns the tuple of (tree_max, dominant_nodes_count)
            of the tree.
            dominant_nodes_count is the number of nodes in the tree
            that are dominant nodes.
            dominant node is a node that is the maximum value in the tree.

            params:
                root: the root of the tree.
            return:
                tuple[int, int]: the tuple of (tree_max, dominant_nodes_count)
                of the tree.
            """

            if not root:
                return (0, 0)

            if not root.left and not root.right:
                return (root.val, 1)

            left: tuple[int, int] = _recursion(root.left)
            right: tuple[int, int] = _recursion(root.right)

            tree_max: int = max(root.val, left[0], right[0])

            return (tree_max, left[1] + right[1] + (root.val == tree_max))

        return _recursion(root)[1]
