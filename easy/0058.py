"""58. Length of Last Word"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0

        for idx in range(1, len(s) + 1):
            if s[-idx] != " ":
                out += 1
            elif s[-idx] == " " and out:
                break

        return out


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
