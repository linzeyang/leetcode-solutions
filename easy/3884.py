"""
3884. First Matching Character From Both Ends

https://leetcode.com/problems/first-matching-character-from-both-ends/

Weekly Contest 495
"""


class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        length: int = len(s)

        for idx, char in enumerate(s):
            if char == s[length - idx - 1]:
                return idx

        return -1
