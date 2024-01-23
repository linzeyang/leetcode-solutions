"""3011. Find if Array Can Be Sorted"""

from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        sections: list[tuple[int, int]] = []
        section: list[int] = [nums[0]]
        target = bin(nums[0]).count("1")

        for idx in range(1, len(nums)):
            new = bin(nums[idx]).count("1")

            if target == new:
                section.append(nums[idx])
            else:
                target = new
                sections.append((min(section), max(section)))
                section = [nums[idx]]

        if len(section) < len(nums):
            sections.append((min(section), max(section)))

        if len(sections) == 1:
            return True

        for idx in range(1, len(sections)):
            if sections[idx][0] < sections[idx - 1][1]:
                return False

        return True
