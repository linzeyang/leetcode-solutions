"""1261. Find Elements in a Contaminated Binary Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self._nums: set[int] = {0}

        root.val = 0

        self._recover(root)

    def find(self, target: int) -> bool:
        return target in self._nums

    def _recover(self, root: TreeNode) -> None:
        if root.left is None and root.right is None:
            return

        if root.left is not None:
            root.left.val = root.val * 2 + 1

            self._nums.add(root.left.val)

            self._recover(root.left)

        if root.right is not None:
            root.right.val = root.val * 2 + 2

            self._nums.add(root.right.val)

            self._recover(root.right)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
