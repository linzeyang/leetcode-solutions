"""1710. Maximum Units on a Truck"""

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        weight = 0
        remaining = truckSize

        ll = sorted(boxTypes, key=lambda lis: lis[1], reverse=True)

        for x, y in ll:
            if remaining <= x:
                weight += remaining * y
                break
            else:
                weight += x * y
                remaining -= x

        return weight
