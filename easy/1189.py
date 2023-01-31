"""1189. Maximum Number of Balloons"""

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cc = Counter(text)

        return min(cc["b"], cc["a"], cc["n"], cc["l"] // 2, cc["o"] // 2)
