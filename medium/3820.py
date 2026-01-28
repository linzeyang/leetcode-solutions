"""3820. Pythagorean Distance Nodes in a Tree"""

from collections import deque
from typing import List


class Solution:
    """
    https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/
    Weekly Contest 486
    """

    def specialNodes(
        self, n: int, edges: List[List[int]], x: int, y: int, z: int
    ) -> int:
        # Step 1: Construct the adjacency list
        adj: list[list[int]] = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Precompute distances from x, y, z (respectively) to all nodes
        def get_distances(node: int) -> list[int]:
            """
            Returns a list of distances from the given node to all other nodes.
            """

            dists: list[int] = [-1] * n
            dists[node] = 0

            queue: deque[int] = deque([node])

            while queue:
                u: int = queue.popleft()

                for neighbor in adj[u]:
                    if dists[neighbor] != -1:
                        continue

                    dists[neighbor] = dists[u] + 1
                    queue.append(neighbor)

            return dists

        dist_x: list[int] = get_distances(node=x)
        dist_y: list[int] = get_distances(node=y)
        dist_z: list[int] = get_distances(node=z)

        # Step 3: Iterate over all nodes and find special ones:
        out: int = 0

        for idx in range(n):
            dx, dy, dz = sorted([dist_x[idx], dist_y[idx], dist_z[idx]])

            if dx**2 + dy**2 == dz**2:
                out += 1

        return out
