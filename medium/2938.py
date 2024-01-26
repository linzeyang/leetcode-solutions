"""2938. Separate Black and White Balls"""


class Solution:
    def minimumSteps(self, s: str) -> int:
        out = dis = 0

        for idx in range(1, len(s) + 1):
            if s[-idx] == "0":
                dis += 1
            else:
                out += dis

        return out
