"""494. Target Sum"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        known_ways: dict[tuple[int, int], int] = {}

        return self.find_ways(nums, 0, target, known_ways)

    def find_ways(
        self,
        nums: list[int],
        start_idx: int,
        target: int,
        known_ways: dict[tuple[int, int], int],
    ) -> int:
        if (start_idx, target) in known_ways:
            return known_ways[(start_idx, target)]

        if start_idx == len(nums) - 1:
            res = (nums[start_idx] == target) + (nums[start_idx] == -target)
            known_ways[(start_idx, target)] = res

            return res

        res = self.find_ways(
            nums, start_idx + 1, target - nums[start_idx], known_ways
        ) + self.find_ways(nums, start_idx + 1, target + nums[start_idx], known_ways)

        known_ways[(start_idx, target)] = res

        return res
