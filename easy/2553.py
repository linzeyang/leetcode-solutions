"""2553. Separate the Digits in an Array"""

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        out = []

        for num in nums:
            out.extend(self._seperate(num))

        return out

    def _seperate(self, num: int) -> list[int]:
        if num < 10:
            return [num]

        return [int(char) for char in str(num)]
