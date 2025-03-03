"""3471. Find the Largest Almost Missing Integer"""

from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        length = len(nums)

        if k == length:
            return max(nums)

        counter: dict[int, int] = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        if k == 1:
            candidates: list[int] = [key for key, val in counter.items() if val == 1]
        else:
            head = nums[0]
            tail = nums[-1]

            candidates: list[int] = []

            if counter[head] == 1:
                candidates.append(head)
            if counter[tail] == 1:
                candidates.append(tail)

        if not candidates:
            return -1

        return max(candidates)
