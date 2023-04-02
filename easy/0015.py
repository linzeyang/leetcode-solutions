"""15. 3Sum"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out: set[tuple[int, int, int]] = set()

        nums.sort()

        for idx in range(len(nums) - 2):
            num_a = nums[idx]

            head = idx + 1
            tail = len(nums) - 1

            while head < tail:
                if nums[head] + nums[tail] == -num_a:
                    out.add((num_a, nums[head], nums[tail]))
                    tail -= 1
                elif nums[head] + nums[tail] > -num_a:
                    tail -= 1
                else:
                    head += 1

        return list(out)
