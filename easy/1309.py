"""1309. Decrypt String from Alphabet to Integer Mapping"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        out = []
        idx = 0

        while idx < len(s):
            if (idx + 2) < len(s) and s[idx + 2] == "#":
                out.append(chr(int(s[idx : idx + 2]) + 96))
                idx += 3
            else:
                out.append(chr(int(s[idx]) + 96))
                idx += 1

        return "".join(out)
