"""1184. Distance Between Bus Stops"""

from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0

        if start > destination:
            start, destination = destination, start

        dis_a = sum(distance[start:destination])

        return min(dis_a, sum(distance) - dis_a)
