"""2947. Count Beautiful Substrings I"""


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        out = 0

        for idx in range(len(s) - 1):
            vow = cons = 0

            for jdx in range(idx, len(s)):
                if s[jdx] in vowels:
                    vow += 1
                else:
                    cons += 1

                if (vow == cons) and (vow**2 % k == 0):
                    out += 1

        return out
