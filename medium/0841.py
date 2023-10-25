"""841. Keys and Rooms"""

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited: set[int] = {0}

        self._visit(rooms=rooms, idx=0, visited=visited)

        return len(rooms) == len(visited)

    def _visit(self, rooms: list[list[int]], idx: int, visited: set[int]) -> None:
        for room in rooms[idx]:
            if room not in visited:
                visited.add(room)
                self._visit(rooms=rooms, idx=room, visited=visited)
