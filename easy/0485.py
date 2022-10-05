"""485. Max Consecutive Ones"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = temp = 0

        for i in nums:
            if i == 1:
                temp += 1
            elif temp != 0:
                if temp > count:
                    count = temp
                temp = 0

        return max(count, temp)
