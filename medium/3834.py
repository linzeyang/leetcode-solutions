"""3834. Merge Adjacent Equal Elements"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/merge-adjacent-equal-elements/
    Weekly Contest 488
    """

    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack: list[int] = []

        for num in nums:
            stack.append(num)

            while len(stack) > 1:
                if stack[-1] != stack[-2]:
                    break

                stack.pop()
                stack[-1] *= 2

        return stack
