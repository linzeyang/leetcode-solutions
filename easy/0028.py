"""28. Find the Index of the First Occurrence in a String"""


# Using string.find()
class SolutionTwo:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# Using iteration
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack) - len(needle) + 1):
            if (
                haystack[idx] == needle[0]
                and haystack[idx : idx + len(needle)] == needle
            ):
                return idx

        return -1
