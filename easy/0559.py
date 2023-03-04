"""559. Maximum Depth of N-ary Tree"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if root is None:
            return 0

        out = 1
        temp = root.children

        while temp:
            out += 1

            temp2 = []

            for node in temp:
                if node.children:
                    temp2.extend(node.children)

            temp = temp2

        return out
