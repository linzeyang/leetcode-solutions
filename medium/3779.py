"""3779. Minimum Number of Operations to Have Distinct Elements"""

import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Traverse the list backwards to find the second appearance of each number.
        If a number appears for the first time, skip it.
        If a number appears for the second time, record its index.
        After the traversal, find the maximum index of second appearances.
        The minimum number of operations is the ceiling of (max_idx + 1) / 3.
        If no number appears for the second time, return 0.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        length: int = len(nums)
        distinct_nums: set[int] = set()
        second_appearance: dict[int, int] = {}

        for idx in range(1, length + 1):
            num: int = nums[-idx]

            if num not in distinct_nums:
                distinct_nums.add(num)
            elif num not in second_appearance:
                second_appearance[num] = length - idx

        if not second_appearance:
            return 0

        max_idx: int = max(second_appearance.values())

        return math.ceil((max_idx + 1) / 3)
