"""95. Unique Binary Search Trees II"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self._generate_trees(start=1, end=n)

    def _generate_trees(self, start: int, end: int) -> list[TreeNode]:
        if start > end:
            return []

        if start == end:
            return [TreeNode(val=start)]

        if end - start == 1:
            return [
                TreeNode(val=start, right=TreeNode(val=end)),
                TreeNode(val=end, left=TreeNode(val=start)),
            ]

        out: list[TreeNode] = []

        for m in range(start, end + 1):
            lefts = self._generate_trees(start=start, end=m - 1)
            rights = self._generate_trees(start=m + 1, end=end)

            if not lefts:
                for ri in rights:
                    out.append(TreeNode(val=m, right=ri))
            elif not rights:
                for le in lefts:
                    out.append(TreeNode(val=m, left=le))
            else:
                for le in lefts:
                    for ri in rights:
                        out.append(TreeNode(val=m, left=le, right=ri))

        return out
