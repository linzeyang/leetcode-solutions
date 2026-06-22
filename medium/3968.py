"""
3968. Maximum Manhattan Distance After All Moves

https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

Weekly Contest 507
"""


class Solution:
    def maxDistance(self, moves: str) -> int:
        horizontal: int = 0
        vertical: int = 0
        num_of_underscore: int = 0

        for mov in moves:
            if mov == "U":
                vertical += 1
            elif mov == "D":
                vertical -= 1
            elif mov == "L":
                horizontal -= 1
            elif mov == "R":
                horizontal += 1
            else:
                num_of_underscore += 1

        return abs(horizontal) + abs(vertical) + num_of_underscore
