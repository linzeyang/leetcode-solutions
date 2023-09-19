"""
28. Find the Index of the First Occurrence in a String
"""


# Using string.find()
class SolutionTwo:
    def strStr(self, haystack: str, needle: str) -> int:
        # Runtime: 31 ms, faster than 93.77% of Python3 online submissions for Find the Index of the First Occurrence in a String.
        # Memory Usage: 13.8 MB, less than 97.22% of Python3 online submissions for Find the Index of the First Occurrence in a String.
        return haystack.find(needle)


# Using iteration
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Runtime: 51 ms, faster than 46.06% of Python3 online submissions for Find the Index of the First Occurrence in a String.
        # Memory Usage: 13.8 MB, less than 64.97% of Python3 online submissions for Find the Index of the First Occurrence in a String.
        len_of_needle = len(needle)

        for i in range(len(haystack) - len_of_needle + 1):
            if needle == haystack[i : i + len_of_needle]:
                return i

        return -1
