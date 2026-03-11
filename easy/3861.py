"""3861. Minimum Capacity Box"""


class Solution:
    """
    https://leetcode.com/problems/minimum-capacity-box/
    Weekly Contest 492
    """

    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        out: int = -1
        current_min: int = 101

        for idx, cap in enumerate(capacity):
            if itemSize <= cap < current_min:
                current_min = cap
                out = idx

        return out
