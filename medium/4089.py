"""
4089. Count Subarrays With Loose Bounds

https://leetcode.com/problems/count-subarrays-with-loose-bounds/

Biweekly Contest 194
"""


class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        out: int = 0
        current: int = 0

        for num in nums:
            if minK <= num <= maxK:
                current += 1
            elif current:
                out += current * (current + 1) // 2
                current = 0

        if current:
            out += current * (1 + current) // 2

        return out
