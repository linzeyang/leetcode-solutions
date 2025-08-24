"""138. Copy List with Random Pointer"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return

        mapping: dict[Node, Node] = {}
        node = head

        while node:
            mapping[node] = Node(node.val, None, None)
            node = node.next

        node = head

        while node:
            if node.next:
                mapping[node].next = mapping[node.next]

            if node.random:
                mapping[node].random = mapping[node.random]

            node = node.next

        return mapping[head]
