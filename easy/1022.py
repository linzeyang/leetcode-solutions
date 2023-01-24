"""1022. Sum of Root To Leaf Binary Numbers"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # listt = self._sub_sum(root)

        # out = 0

        # for lis in listt:
        #     out += int("".join(lis[::-1]), base=2)

        return sum(int("".join(lis[::-1]), base=2) for lis in self._sub_sum(root))

    def _sub_sum(self, root: TreeNode | None) -> list:
        if root is None:
            return []

        l1, l2 = self._sub_sum(root.left), self._sub_sum(root.right)

        if not l1 and not l2:
            return [[str(root.val)]]

        for lis in l1:
            lis.append(str(root.val))

        for lis in l2:
            lis.append(str(root.val))

        return l1 + l2
