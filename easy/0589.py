"""589. N-ary Tree Preorder Traversal"""

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node | None) -> List[int]:
        if root is None:
            return []

        ll = [root.val]

        for child in root.children:
            ll.extend(self.preorder(child))

        return ll
