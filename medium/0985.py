"""985. Sum of Even Numbers After Queries"""

from typing import List


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        out: list[int] = []

        sum_of_even = sum(num for num in nums if num % 2 == 0)

        for val, idx in queries:
            ori = nums[idx]
            new = ori + val
            nums[idx] = new

            if ori % 2:
                if val % 2:
                    sum_of_even += new
            else:
                if val % 2:
                    sum_of_even -= ori
                else:
                    sum_of_even += val

            out.append(sum_of_even)

        return out
