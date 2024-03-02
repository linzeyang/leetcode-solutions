"""1305. All Elements in Two Binary Search Trees"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lis1 = self._traverse(root1)
        lis2 = self._traverse(root2)

        idx = jdx = 0

        out: list[int] = []

        while idx < len(lis1) and jdx < len(lis2):
            if lis1[idx] < lis2[jdx]:
                out.append(lis1[idx])
                idx += 1
            else:
                out.append(lis2[jdx])
                jdx += 1

        if idx >= len(lis1):
            out.extend(lis2[jdx:])
        else:
            out.extend(lis1[idx:])

        return out

    def _traverse(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        return self._traverse(root.left) + [root.val] + self._traverse(root.right)
