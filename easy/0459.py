"""459. Repeated Substring Pattern"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for idx in range(len(s) // 2):
            if len(s) % (idx + 1) == 0 and s[: idx + 1] * (len(s) // (idx + 1)) == s:
                return True

        return False
