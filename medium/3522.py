"""3522. Calculate Score After Performing Instructions"""

from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        idx = 0

        visited: set[int] = set()

        while 0 <= idx < len(instructions):
            if idx in visited:
                break

            visited.add(idx)

            if instructions[idx] == "add":
                score += values[idx]
                idx += 1
            else:
                idx += values[idx]

        return score
