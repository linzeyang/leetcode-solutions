"""496. Next Greater Element I"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping: dict[int, int] = {}
        stack: list[int] = []

        for num in nums2[::-1]:
            while stack and num >= stack[-1]:
                stack.pop(-1)

            mapping[num] = stack[-1] if stack else -1
            stack.append(num)

        return [mapping[num] for num in nums1]
