"""3396. Minimum Number of Operations to Make Elements in Array Distinct"""

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        out = 0

        counter: dict[int, int] = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        idx = 0

        while any(val > 1 for val in counter.values()):
            out += 1

            if idx >= len(nums) - 2:
                break

            for _ in range(3):
                counter[nums[idx]] -= 1
                idx += 1

        return out
