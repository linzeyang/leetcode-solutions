"""2583. Kth Largest Sum in a Binary Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        sums = []
        level = [root]

        while level:
            sums.append(sum(node.val for node in level))

            temp_level = []

            for node in level:
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right)

            level = temp_level

        if k > len(sums):
            return -1

        return sorted(sums)[-k]
