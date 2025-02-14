"""1910. Remove All Occurrences of a Substring"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while (idx := s.find(part)) >= 0:
            s = s[:idx] + s[idx + len(part) :]

        return s
