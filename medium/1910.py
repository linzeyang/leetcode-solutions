"""1910. Remove All Occurrences of a Substring"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = "".join(s.split(part, 1))

        return s
