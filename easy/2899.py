"""2899. Last Visited Integers"""

from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        stack: list[int] = []
        idx = -1
        out: list[int] = []

        for word in words:
            if word.isdigit():
                idx = -1
                stack.append(int(word))
            else:
                if len(stack) + idx < 0:
                    out.append(-1)
                else:
                    out.append(stack[idx])
                    idx -= 1

        return out
