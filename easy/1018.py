"""1018. Binary Prefix Divisible By 5"""

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        out: list[bool] = []
        mod: int = 0

        for num in nums:
            # Instead of using a variable to store the number,
            # we can use modulo to keep the number within the range of 0-4.
            # This approach overcomes the overhead of storing/calculating large numbers.
            mod = (2 * mod + num) % 5
            out.append(mod == 0)

        return out
