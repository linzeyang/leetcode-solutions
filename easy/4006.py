"""
4006. Count Valid Prefixes

https://leetcode.com/problems/count-valid-prefixes/

Biweekly Contest 188
"""


class Solution:
    def countValidPrefixes(self, s: str) -> int:
        counter: list[int] = [0, 0]

        out: int = 0

        for char in s:
            if char == "0":
                counter[0] += 1
            else:
                counter[1] += 1

            if abs(counter[0] - counter[1]) <= 1:
                out += 1

        return out
