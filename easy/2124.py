"""2124. Check if All A's Appears Before All B's"""


class Solution:
    def checkString(self, s: str) -> bool:
        try:
            idx = s.index("b")
        except ValueError:
            return True

        for i in range(idx + 1, len(s)):
            if s[i] == "a":
                return False

        return True
