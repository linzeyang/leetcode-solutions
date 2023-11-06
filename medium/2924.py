"""2924. Find Champion II"""

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree: list[int] = [0] * n

        for _, team_b in edges:
            in_degree[team_b] += 1

        champions = [idx for idx, degree in enumerate(in_degree) if not degree]

        return champions[0] if len(champions) == 1 else -1
