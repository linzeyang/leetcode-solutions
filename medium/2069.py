"""
2069. Walking Robot Simulation II

https://leetcode.com/problems/walking-robot-simulation-ii/

Biweekly Contest 65
"""

from typing import List


class Robot:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.steps: int = 0
        self.have_moved: bool = False

    def step(self, num: int) -> None:
        self.have_moved = True
        self.steps = (self.steps + num) % (self.width * 2 + self.height * 2 - 4)

    def getPos(self) -> List[int]:
        if self.steps <= self.width - 1:
            return [self.steps, 0]
        elif self.steps <= self.width + self.height - 2:
            return [self.width - 1, self.steps - self.width + 1]
        elif self.steps <= self.width * 2 + self.height - 3:
            return [self.width * 2 + self.height - self.steps - 3, self.height - 1]
        else:
            return [0, self.width * 2 + self.height * 2 - self.steps - 4]

    def getDir(self) -> str:
        if self.steps == 0:
            return "East" if not self.have_moved else "South"
        if self.steps <= self.width - 1:
            return "East"
        if self.steps <= self.width + self.height - 2:
            return "North"
        if self.steps <= self.width * 2 + self.height - 3:
            return "West"
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
