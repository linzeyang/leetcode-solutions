"""
3992. Rearrange String to Avoid Character Pair

https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

Biweekly Contest 187
"""

from collections import Counter


class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        counter: Counter[str] = Counter(s)
        parts: list[str] = [y * counter[y], x * counter[x]]

        for char in counter:
            if char not in (x, y):
                parts.append(char * counter[char])

        return "".join(parts)
