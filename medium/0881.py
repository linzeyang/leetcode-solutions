"""881. Boats to Save People"""

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people_mapping: dict[int, int] = {}

        for weight in people:
            if weight not in people_mapping:
                people_mapping[weight] = 1
            else:
                people_mapping[weight] += 1

        out = 0

        for weight in range(limit, 0, -1):
            if weight not in people_mapping or not people_mapping[weight]:
                continue

            while people_mapping[weight]:
                people_mapping[weight] -= 1

                if weight == limit:
                    out += 1
                    continue

                for weight2 in range(limit - weight, 0, -1):
                    if weight2 not in people_mapping or not people_mapping[weight2]:
                        continue

                    people_mapping[weight2] -= 1
                    break
                out += 1

        return out
