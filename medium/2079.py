"""2079. Watering Plants"""

from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur_pos = 0
        cur_vol = capacity - plants[0]

        out = 1

        while cur_pos < len(plants) - 1:
            target = plants[cur_pos + 1]

            if cur_vol >= target:
                cur_vol -= target
                out += 1
            else:
                cur_vol = capacity - target
                out += 2 * cur_pos + 3

            cur_pos += 1

        return out
