"""2535. Difference Between Element Sum and Digit Sum of an Array"""

from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_one = sum(nums)
        sum_two = sum(self._digit_sum(num) for num in nums)

        return abs(sum_one - sum_two)

    def _digit_sum(self, num: int) -> int:
        if num < 10:
            return num

        return sum(int(char) for char in str(num))
