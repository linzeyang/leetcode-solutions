"""1079. Letter Tile Possibilities"""

from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        possibles: set = set()

        for length in range(1, len(tiles) + 1):
            for possible in permutations(tiles, length):
                possibles.add(possible)

        return len(possibles)
