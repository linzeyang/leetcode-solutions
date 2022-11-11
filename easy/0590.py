"""590. N-ary Tree Postorder Traversal"""

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node | None) -> List[int]:
        if root is None:
            return []

        ll = []

        for child in root.children:
            ll.extend(self.postorder(child))

        ll.append(root.val)

        return ll
