"""1578. Minimum Time to Make Rope Colorful"""

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        length: int = len(colors)

        if length == 1:
            return 0

        left: int = 0
        right: int = 1
        out: int = 0

        while right < length:
            if colors[right] == colors[left]:
                right += 1
            else:
                if right - left > 1:
                    out += sum(neededTime[left:right]) - max(neededTime[left:right])

                left = right
                right += 1

        if right - left > 1:
            out += sum(neededTime[left:right]) - max(neededTime[left:right])

        return out
