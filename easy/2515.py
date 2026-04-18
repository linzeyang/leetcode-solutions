"""
2515. Shortest Distance to Target String in a Circular Array

https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

Weekly Contest 325
"""

from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        length: int = len(words)
        out: int = length

        for idx, word in enumerate(words):
            if word == target:
                out = min(
                    out, min(abs(idx - startIndex), length - abs(idx - startIndex))
                )

        return out if out < length else -1
