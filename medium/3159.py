"""3159. Find Occurrences of an Element in an Array"""

from typing import List


class Solution:
    def occurrencesOfElement(
        self, nums: List[int], queries: List[int], x: int
    ) -> List[int]:
        occur: list[int] = [idx for idx, num in enumerate(nums) if num == x]

        return [occur[query - 1] if query <= len(occur) else -1 for query in queries]
