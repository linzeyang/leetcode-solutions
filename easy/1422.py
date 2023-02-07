"""1422. Maximum Score After Splitting a String"""


class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) == 2:
            return (s[0] == "0") + (s[1] == "1")
        return max(s[:i].count("0") + s[i:].count("1") for i in range(1, len(s)))
