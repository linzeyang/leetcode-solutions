"""547. Number of Provinces"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        relations: dict[int, int] = {}

        for city1, row in enumerate(isConnected):
            if city1 not in relations:
                relations[city1] = city1

            city1_ancestor = self._find_ancestor(city1, relations)

            for city2, connected in enumerate(row):
                if city2 == city1 or not connected:
                    continue

                if city2 not in relations:
                    relations[city2] = city1_ancestor
                else:
                    city2_ancestor = self._find_ancestor(city2, relations)

                    if city2_ancestor != city1_ancestor:
                        relations[city2_ancestor] = city1_ancestor

        return sum(1 for k, v in relations.items() if k == v)

    def _find_ancestor(self, city: int, relations: dict[int, int]) -> int:
        while (ancestor := relations[city]) != city:
            city = ancestor

        return city
