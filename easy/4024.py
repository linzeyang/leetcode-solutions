"""
4024. Nearest Available Drone

https://leetcode.com/problems/nearest-available-drone/

Weekly Contest 515
"""


class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        target_x, target_y = target

        out: int = -1
        min_distance: int = 101

        for idx, (x, y, r) in enumerate(drones):
            distance: int = abs(x - target_x) + abs(y - target_y)

            if distance <= r and distance < min_distance:
                min_distance = distance
                out = idx

        return out
