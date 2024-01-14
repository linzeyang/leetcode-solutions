"""1347. Minimum Number of Steps to Make Two Strings Anagram"""

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)

        out = 0

        for k, v in counter_t.items():
            if k not in counter_s:
                out += v
            elif k in counter_s and v > counter_s[k]:
                out += v - counter_s[k]

        return out
