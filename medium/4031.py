"""
4031. Find All Numbers Disappeared in an Array II

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/

Weekly Contest 516
"""


class Solution:
    def findDisappearedNumbers(
        self, nums: list[int], lower: int, upper: int
    ) -> list[list[int]]:
        nums: list[int] = sorted(set(nums))

        out: list[list[int]] = []

        current: int = lower

        for num in nums:
            if num < lower or num > upper:
                continue

            if num == current:
                current += 1
            else:
                out.append([current, num - 1])
                current = num + 1

        if current <= upper:
            out.append([current, upper])

        return out
