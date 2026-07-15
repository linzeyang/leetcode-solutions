"""
3987. Minimum Total Cost to Process All Elements

https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

Weekly Contest 510
"""

from math import ceil


class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        total_ops: int = 0
        resources: int = k

        for num in nums:
            if num <= resources:
                resources -= num
            else:
                num_ops: int = ceil((num - resources) / k)
                total_ops += num_ops
                resources += num_ops * k - num

        cost: int = (1 + total_ops) * total_ops // 2

        return cost % (1_000_000_000 + 7)
