"""3178. Find the Child Who Has the Ball After K Seconds"""


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        direction = -1
        idx = 0

        for _ in range(k):
            if idx in (0, n - 1):
                direction = -direction

            idx += direction

        return idx
