"""
2287. Rearrange Characters to Make Target String

https://leetcode.com/problems/rearrange-characters-to-make-target-string/

Weekly Contest 295
"""

from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter: Counter[str] = Counter(s)
        target_counter: Counter[str] = Counter(target)

        return min(counter[char] // freq for char, freq in target_counter.items())
