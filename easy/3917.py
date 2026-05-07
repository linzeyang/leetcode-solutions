"""
3917. Count Indices With Opposite Parity

https://leetcode.com/problems/count-indices-with-opposite-parity/

Weekly Contest 500
"""


class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        counter: dict[int, int] = {0: 0, 1: 0}
        out: list[int] = []

        for num in reversed(nums):
            parity: int = num & 1

            out.append(counter[not parity])
            counter[parity] += 1

        return out[::-1]
