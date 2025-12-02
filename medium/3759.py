"""3759. Count Elements With at Least K Greater Values"""

from collections import Counter
from typing import List


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if not k:
            return len(nums)

        counter: Counter[int] = Counter(nums)
        keys: list[int] = sorted(counter.keys(), reverse=True)

        accumulated: int = 0

        for key in keys:
            accumulated += counter[key]

            if accumulated >= k:
                return len(nums) - accumulated

        return 0
