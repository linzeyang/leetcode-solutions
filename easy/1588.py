"""1588. Sum of All Odd Length Subarrays"""

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        out = 0

        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) - i + 1):
                out += sum(arr[j: j + i])

        return out
