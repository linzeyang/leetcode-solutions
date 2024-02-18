"""429. N-ary Tree Level Order Traversal"""

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        out: list[list[int]] = []
        level: list[Node] = [root]

        while level:
            out.append([node.val for node in level])
            temp_level: list[Node] = []

            for node in level:
                if node.children:
                    temp_level.extend(node.children)

            level = temp_level

        return out
