"""133. Clone Graph"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        new = Node(val=1)

        contained_nodes: dict[int, "Node"] = {1: new}

        new.neighbors = [
            self.clone_graph(neighbor, contained_nodes) for neighbor in node.neighbors
        ]

        return new

    def clone_graph(self, node: "Node", contained_nodes: dict[int, "Node"]) -> "Node":
        if node.val in contained_nodes:
            return contained_nodes[node.val]

        new = Node(val=node.val)

        contained_nodes[node.val] = new

        new.neighbors = [
            self.clone_graph(neighbor, contained_nodes) for neighbor in node.neighbors
        ]

        return new
