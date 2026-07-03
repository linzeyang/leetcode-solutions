"""
3965. Finish Time of Tasks I

https://leetcode.com/problems/finish-time-of-tasks-i/

Biweekly Contest 185
"""

from typing import List


class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        mapping: dict[int, list[int]] = {}

        for parent, child in edges:
            mapping.setdefault(parent, []).append(child)

        # finish time of each node
        finish: list[int] = [0] * n

        # iterative post-order traversal,
        # avoids potential stack overflow risk of using recursive function
        stack: list[tuple[int, bool]] = [(0, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                children: list[int] = mapping.get(node, [])

                if not children:
                    finish[node] = baseTime[node]
                else:
                    children_times: list[int] = [finish[child] for child in children]
                    own_duration: int = (
                        max(children_times) - min(children_times) + baseTime[node]
                    )
                    finish[node] = max(children_times) + own_duration
            else:
                stack.append((node, True))

                for child in mapping.get(node, []):
                    stack.append((child, False))

        return finish[0]
