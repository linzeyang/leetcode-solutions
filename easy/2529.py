"""2529. Maximum Count of Positive Integer and Negative Integer"""

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        length = len(nums)

        if nums[0] > 0 or nums[-1] < 0:
            return length

        if nums[0] == 0:
            for i in range(length):
                if nums[i] > 0:
                    return length - i
            return 0

        if nums[-1] == 0:
            for i in range(length):
                if nums[-i - 1] < 0:
                    return length - i
            return 0

        neg = pos = -1

        for i in range(length):
            if nums[i] == 0 and neg == -1:
                neg = i
            elif nums[i] > 0 and pos == -1:
                pos = length - i
                if neg == -1:
                    neg = i

            if neg >= 0 and pos >= 0:
                break

        return max(neg, pos)
