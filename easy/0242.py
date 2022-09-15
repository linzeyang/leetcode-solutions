"""
242. Valid Anagram
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Very slow:
        # Runtime: 123 ms, faster than 9.58% of Python3 online submissions for Valid Anagram.
        # Memory Usage: 14.4 MB, less than 67.08% of Python3 online submissions for Valid Anagram.
        if len(s) != len(t):
            return False

        tempa = {}
        tempb = {}

        for i in range(len(s)):
            if (p := s[i]) not in tempa:
                tempa[p] = 1
            else:
                tempa[p] += 1

            if (q := t[i]) not in tempb:
                tempb[q] = 1
            else:
                tempb[q] += 1

        return tempa == tempb
