"""2391. Minimum Amount of Time to Collect Garbage"""

from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        trucks: dict[str, int] = {
            "M": 0,
            "P": 0,
            "G": 0,
        }

        last_present: dict[str, int] = {
            "M": -1,
            "P": -1,
            "G": -1,
        }

        for idx, house in enumerate(garbage):
            for gar in house:
                last_present[gar] = idx
                trucks[gar] += 1

            if idx == len(travel):
                break

            for truck in trucks:
                trucks[truck] += travel[idx]

        for gar, last in last_present.items():
            if last == -1:
                trucks[gar] = 0
            else:
                trucks[gar] -= sum(travel[last:])

        return sum(trucks.values())
