"""2957. Remove Adjacent Almost-Equal Characters"""


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        if len(word) == 1:
            return 0

        out = 0
        idx = 1

        while idx < len(word):
            if -1 <= ord(word[idx]) - ord(word[idx - 1]) <= 1:
                out += 1
                idx += 2
            else:
                idx += 1

        return out
