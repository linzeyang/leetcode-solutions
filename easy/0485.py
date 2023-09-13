"""485. Max Consecutive Ones"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = current = 0

        for num in nums:
            if num:
                current += 1
            elif not num and current:
                if current > maxx:
                    maxx = current
                current = 0

        if current > maxx:
            maxx = current

        return maxx
