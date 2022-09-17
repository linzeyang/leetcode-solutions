"""
392. Is Subsequence
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Very slow:
        # Runtime: 71 ms, faster than 13.00% of Python3 online submissions for Is Subsequence.
        # Memory Usage: 13.9 MB, less than 42.87% of Python3 online submissions for Is Subsequence.
        idx = 0

        for char in s:
            try:
                i = t.index(char, idx)
            except ValueError:
                return False

            idx = i + 1

        return True
