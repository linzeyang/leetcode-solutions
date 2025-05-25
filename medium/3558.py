"""3558. Number of Ways to Assign Edge Weights I"""

from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        edges.sort(key=lambda item: item[0])

        node_level: dict[int, int] = {1: 0}

        connections: dict[int, list[int]] = {}

        for a, b in edges:
            if a not in connections:
                connections[a] = [b]
            else:
                connections[a].append(b)

        for node, conns in connections.items():
            for x in conns:
                node_level[x] = node_level[node] + 1

        max_level: int = max(node_level.values())

        return 2 ** (max_level - 1) % (int(1e9) + 7)
