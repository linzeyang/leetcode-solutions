"""392. Is Subsequence"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0

        for char in s:
            try:
                i = t.index(char, idx)
            except ValueError:
                return False

            idx = i + 1

        return True
