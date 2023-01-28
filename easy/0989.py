"""989. Add to Array-Form of Integer"""

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for idx in range(-1, -len(num) - 1, -1):
            quotient, remaining = divmod(num[idx] + k, 10)

            num[idx] = remaining

            if quotient == 0:
                k = 0
                break

            k = quotient

        while k > 0:
            quotient, remaining = divmod(k, 10)
            num.insert(0, remaining)
            k = quotient

        return num
