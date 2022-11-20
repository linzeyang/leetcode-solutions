"""2475. Number of Unequal Triplets in Array"""

from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        out = 0
        length = len(nums)

        for i in range(length - 2):
            a = nums[i]

            for j in range(i + 1, length - 1):
                if (b := nums[j]) != a:
                    for k in range(j + 1, length):
                        if nums[k] not in {a, b}:
                            out += 1
                            print(a, b, nums[k])

        return out
