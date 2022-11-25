"""2265. Count Nodes Equal to Average of Subtree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self._count = 0
        self._do_calc(root)
        return self._count

    def _do_calc(self, node: Optional[TreeNode]) -> tuple[int, int]:
        if node is None:
            return 0, 0

        if node.left is None and node.right is None:
            self._count += 1
            print(f"node: {node.val}, {self._count=}")
            return node.val, 1

        sub_sum_1, num_of_nodes_1 = self._do_calc(node.left)
        sub_sum_2, num_of_nodes_2 = self._do_calc(node.right)
        summ = node.val + sub_sum_1 + sub_sum_2
        num_of_nodes = 1 + num_of_nodes_1 + num_of_nodes_2

        if node.val == summ // num_of_nodes:
            self._count += 1

        print(f"node: {node.val}, {summ=}, {self._count=}")

        return summ, num_of_nodes
