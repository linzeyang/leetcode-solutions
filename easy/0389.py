"""
389. Find the Difference
"""


class SolutionTwo:
    def findTheDifference(self, s: str, t: str) -> str:
        # This is faster:
        # Runtime: 42 ms, faster than 83.10% of Python3 online submissions for Find the Difference.
        # Memory Usage: 13.8 MB, less than 76.38% of Python3 online submissions for Find the Difference.
        for char in t:
            if t.count(char) != s.count(char):
                return char


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Runtime: 54 ms, faster than 59.42% of Python3 online submissions for Find the Difference.
        # Memory Usage: 14.1 MB, less than 32.16% of Python3 online submissions for Find the Difference.
        out = list(t)

        for char in s:
            out.remove(char)

        return out[0]
