"""398. Random Pick Index"""

from random import choice
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self._con = {}

        for idx, num in enumerate(nums):
            if num not in self._con:
                self._con[num] = [idx]
            else:
                self._con[num].append(idx)

    def pick(self, target: int) -> int:
        return choice(self._con[target])  # noqa: S311


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
