"""
4065. Rearrange Array by Removing Distinct Values

https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/

Weekly Contest 521
"""


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans: list[int] = []

        while nums:
            distinct: set[int] = set()
            remaining: list[int] = []

            for num in nums:
                if num not in distinct:
                    distinct.add(num)
                else:
                    remaining.append(num)

            ans.extend(sorted(distinct))
            nums = remaining

        return ans
