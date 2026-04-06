"""
874. Walking Robot Simulation

https://leetcode.com/problems/walking-robot-simulation/

Weekly Contest 94
"""

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions: tuple[tuple[int, int], ...] = ((0, 1), (1, 0), (0, -1), (-1, 0))
        obstacle_set: set[tuple[int, int]] = {(x, y) for x, y in obstacles}

        x: int = 0
        y: int = 0
        dir_idx: int = 0
        out: int = 0

        for cmd in commands:
            match cmd:
                case -2:
                    dir_idx = (dir_idx - 1) % 4
                case -1:
                    dir_idx = (dir_idx + 1) % 4
                case _:
                    dx, dy = directions[dir_idx]

                    for _ in range(cmd):
                        if (x + dx, y + dy) in obstacle_set:
                            break

                        x += dx
                        y += dy

                        out = max(out, x * x + y * y)

        return out
