"""2582. Pass the Pillow"""

# This question is the same as 3178: Find the Child Who Has the Ball After K Seconds.


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        div, mod = divmod(time, n - 1)

        if div & 1:
            return n - mod

        return 1 + mod
