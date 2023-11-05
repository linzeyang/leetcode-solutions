"""802. Find Eventual Safe States"""

from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        mapping: dict[int, list[int]] = {}
        in_degree: list[int] = [0] * len(graph)

        for idx, nodes in enumerate(graph):
            for node in nodes:
                if node not in mapping:
                    mapping[node] = [idx]
                else:
                    mapping[node].append(idx)
                in_degree[idx] += 1

        queue = deque()

        for idx, degree in enumerate(in_degree):
            if not degree:
                queue.append(idx)

        safe_nodes: list[int] = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)

            if node not in mapping:
                continue

            for parent_node in mapping[node]:
                in_degree[parent_node] -= 1

                if not in_degree[parent_node]:
                    queue.append(parent_node)

        return sorted(safe_nodes)
