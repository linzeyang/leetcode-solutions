"""576. Out of Boundary Paths"""


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        return self._find_paths(m, n, maxMove, startRow, startColumn, {})

    def _find_paths(
        self,
        m: int,
        n: int,
        maxMove: int,
        startRow: int,
        startColumn: int,
        memory: dict[tuple[int, int, int], int],
    ) -> int:
        if maxMove <= 0:
            return 0

        if (startRow, startColumn, maxMove) in memory:
            return memory[(startRow, startColumn, maxMove)]

        out = 0

        if startRow == 0:
            out += 1
        else:
            out += self._find_paths(
                m, n, maxMove - 1, startRow - 1, startColumn, memory
            )

        if startRow == m - 1:
            out += 1
        else:
            out += self._find_paths(
                m, n, maxMove - 1, startRow + 1, startColumn, memory
            )

        if startColumn == 0:
            out += 1
        else:
            out += self._find_paths(
                m, n, maxMove - 1, startRow, startColumn - 1, memory
            )

        if startColumn == n - 1:
            out += 1
        else:
            out += self._find_paths(
                m, n, maxMove - 1, startRow, startColumn + 1, memory
            )

        memory[(startRow, startColumn, maxMove)] = out

        return out % int(1e9 + 7)
