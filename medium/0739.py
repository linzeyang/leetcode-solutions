"""739. Daily Temperatures"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[int] = []
        out: list[int] = []

        for idx in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[idx] >= temperatures[stack[-1]]:
                stack.pop()

            out.append(stack[-1] - idx if stack else 0)

            stack.append(idx)

        return out[::-1]
