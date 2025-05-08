"""501. Find Mode in Binary Search Tree"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        all_vals: list[int] = self._traverse(root)
        counter: dict[int, int] = {}

        for val in all_vals:
            if val not in counter:
                counter[val] = 1
            else:
                counter[val] += 1

        max_freq = max(counter.values())

        return [key for key, val in counter.items() if val == max_freq]

    def _traverse(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        return self._traverse(root.left) + [root.val] + self._traverse(root.right)
