"""657. Robot Return to Origin"""

from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cc = Counter(moves)

        return cc["L"] == cc["R"] and cc["U"] == cc["D"]
