"""
58. Length of Last Word
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # This may be faster than the other solution
        # return len(s.split()[-1])

        index = len(s) - 1
        counter = 0

        while index >= 0:
            if s[index] == " ":
                if counter:
                    break
                index -= 1
            else:
                counter += 1
                index -= 1

        return counter
