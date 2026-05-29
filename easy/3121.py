"""
3121. Count the Number of Special Characters II

https://leetcode.com/problems/count-the-number-of-special-characters-ii/

Weekly Contest 394
"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mapping: dict[str, int] = {}

        for idx, char in enumerate(word):
            if char.islower():  # last occurrence of lower case letter
                mapping[char] = idx
            elif char not in mapping:  # first occurrence of upper case letter
                mapping[char] = idx

        out: int = 0

        for char, idx in mapping.items():
            if char.islower() and idx < mapping.get(char.upper(), 0):
                out += 1

        return out
