"""1710. Maximum Units on a Truck"""

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda lis: lis[1], reverse=True)

        num_all = unit_all = 0

        for num, capacity in boxTypes:
            if num >= truckSize - num_all:
                unit_all += (truckSize - num_all) * capacity
                return unit_all

            num_all += num
            unit_all += num * capacity

        return unit_all
