"""213. House Robber II"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        dic = {
            0: (nums[0], 0),
            1: (nums[1], nums[1]),
            2: (nums[0] + nums[2], nums[2]),
        }

        for idx in range(3, len(nums)):
            prev1 = dic[idx - 3]
            prev2 = dic[idx - 2]

            dic[idx] = (
                nums[idx] + max(prev1[0], prev2[0]),
                nums[idx] + max(prev1[1], prev2[1]),
            )

        return max(
            dic[len(nums) - 3][0],
            dic[len(nums) - 3][1],
            dic[len(nums) - 2][0],
            dic[len(nums) - 2][1],
            dic[len(nums) - 1][1],
        )
