"""2415. Reverse Odd Levels of Binary Tree"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        level = [root]
        is_odd = False

        while level:
            if is_odd:
                rev = [node.val for node in reversed(level)]
                for idx in range(len(level)):
                    level[idx].val = rev[idx]

            temp_level: list[TreeNode] = []

            for node in level:
                if node.left:
                    temp_level.append(node.left)
                    temp_level.append(node.right)

            level = temp_level
            is_odd = not is_odd

        return root
