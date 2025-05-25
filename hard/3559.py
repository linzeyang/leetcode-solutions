"""3559. Number of Ways to Assign Edge Weights II"""

from typing import List


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        edges.sort(key=lambda item: item[0])

        node_level: dict[int, int] = {1: 0}

        connections: dict[int, list[int]] = {}

        child_parent: dict[int, int] = {}

        for a, b in edges:
            if a not in connections:
                connections[a] = [b]
            else:
                connections[a].append(b)

            child_parent[b] = a

        for node, conns in connections.items():
            for x in conns:
                node_level[x] = node_level[node] + 1

        out: list[int] = []
        DIVISOR = int(1e9) + 7

        for x, y in queries:
            if x == y:
                out.append(0)
                continue

            x_level: int = node_level[x]
            y_level: int = node_level[y]

            counter = abs(x_level - y_level)

            if x_level > y_level:
                for _ in range(counter):
                    x = child_parent[x]
            elif x_level < y_level:
                for _ in range(counter):
                    y = child_parent[y]

            while x != y:
                x = child_parent[x]
                y = child_parent[y]
                counter += 2

            out.append(2 ** (counter - 1) % DIVISOR)

        return out
