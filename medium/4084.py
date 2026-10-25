"""
4084. Last Visited Cell in a Directional Grid

https://leetcode.com/problems/last-visited-cell-in-a-directional-grid/

Weekly Contest 524
"""


class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        height: int = len(grid)
        width: int = len(grid[0])
        visited: set[tuple[int, int]] = {(0, 0)}

        current_x, current_y = 0, 0

        while True:
            cmd: str = grid[current_x][current_y]

            if cmd == "L":
                next_x: int = current_x
                next_y: int = current_y - 1
            elif cmd == "R":
                next_x: int = current_x
                next_y: int = current_y + 1
            elif cmd == "U":
                next_x: int = current_x - 1
                next_y: int = current_y
            else:
                next_x: int = current_x + 1
                next_y: int = current_y

            if (
                (next_x, next_y) in visited
                or next_x < 0
                or next_x >= height
                or next_y < 0
                or next_y >= width
            ):
                break

            visited.add((next_x, next_y))
            current_x = next_x
            current_y = next_y

        return [current_x, current_y]
