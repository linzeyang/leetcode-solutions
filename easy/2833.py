"""2833. Furthest Point From Origin"""


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        num_l = moves.count("L")
        num_r = moves.count("R")
        num__ = len(moves) - num_l - num_r

        if num_l == num_r:
            return num__

        return abs(num_l - num_r) + num__
