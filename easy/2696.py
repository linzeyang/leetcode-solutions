"""2696. Minimum String Length After Removing Substrings"""


class Solution:
    def minLength(self, s: str) -> int:
        while (a := "AB" in s) or "CD" in s:
            if a:
                s = s.replace("AB", "")
            else:
                s = s.replace("CD", "")

        return len(s)
