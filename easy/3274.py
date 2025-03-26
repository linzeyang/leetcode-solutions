"""3274. Check if Two Chessboard Squares Have the Same Color"""


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return self._calc_num(coordinate1) & 1 == self._calc_num(coordinate2) & 1

    @staticmethod
    def _calc_num(coordinate: str) -> int:
        char = coordinate[0]
        digit = int(coordinate[1])

        return ord(char) - ord("a") + digit
