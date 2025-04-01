"""3503. Longest Palindrome After Substring Concatenation I"""


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        out = 1

        lens = len(s)
        lent = len(t)

        for sdxi in range(lens):
            for sdxj in range(sdxi, lens + 1):
                spart = s[sdxi:sdxj]

                for tdxi in range(lent):
                    for tdxj in range(tdxi, lent + 1):
                        tpart = t[tdxi:tdxj]

                        if spart + tpart == (spart + tpart)[::-1]:
                            out = max(out, len(spart + tpart))

        return out
