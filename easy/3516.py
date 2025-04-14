"""3516. Find Closest Person"""


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        absx = abs(x - z)
        absy = abs(y - z)

        if absx < absy:
            return 1

        if absx > absy:
            return 2

        return 0
