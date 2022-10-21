"""2357. Make Array Zero by Subtracting Equal Amounts"""

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(n for n in nums if n > 0))
