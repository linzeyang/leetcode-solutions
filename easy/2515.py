"""2515. Shortest Distance to Target String in a Circular Array"""

from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        try:
            target_index = words.index(target)
        except ValueError:
            return -1

        length = len(words)
        out = -1

        for i in range(target_index, length):
            if words[i] == target:
                if (distance := abs(i - startIndex)) > length // 2:
                    distance = length - distance
                if out == -1 or distance < out:
                    out = distance

        return out
