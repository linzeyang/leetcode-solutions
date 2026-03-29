"""
3880. Minimum Absolute Difference Between Two Values

https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

Biweekly Contest 179
"""


class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        last_one: int | None = None
        last_two: int | None = None
        out: int = -1

        for idx, num in enumerate(nums):
            if num == 1:
                last_one = idx

                if last_two is not None:
                    if out == -1:
                        out = idx - last_two
                    else:
                        out = min(out, idx - last_two)
            elif num == 2:
                last_two = idx

                if last_one is not None:
                    if out == -1:
                        out = idx - last_one
                    else:
                        out = min(out, idx - last_one)

        return out
