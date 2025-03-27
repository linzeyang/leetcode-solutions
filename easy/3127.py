"""3127. Make a Square with the Same Color"""

from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for idx in range(2):
            for jdx in range(2):
                num_of_black = (
                    grid[idx][jdx],
                    grid[idx][jdx + 1],
                    grid[idx + 1][jdx],
                    grid[idx + 1][jdx + 1],
                ).count("B")

                if num_of_black != 2:
                    return True

        return False
