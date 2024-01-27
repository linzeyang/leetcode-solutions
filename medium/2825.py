"""2825. Make String a Subsequence Using Cyclic Increments"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False

        idx = 0

        for char in str2:
            alt = chr(ord(char) - 1) if char != "a" else "z"
            found = False

            while idx < len(str1):
                if str1[idx] in {char, alt}:
                    idx += 1
                    found = True
                    break
                else:
                    idx += 1

            if not found:
                return False

        return True
