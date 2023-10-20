"""946. Validate Stack Sequences"""

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack: list[int] = []
        idx = 0

        for num in pushed:
            stack.append(num)

            while stack:
                if stack[-1] != popped[idx]:
                    break
                stack.pop()
                idx += 1

        return idx >= len(popped)
