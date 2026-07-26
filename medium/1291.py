"""
1291. Sequential Digits

https://leetcode.com/problems/sequential-digits/

Weekly Contest 167
"""

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        out: list[int] = []

        for length in range(len(str(low)), len(str(high)) + 1):
            candidate: int = int("".join(str(digit) for digit in range(1, length + 1)))

            for _ in range(10 - length):
                if candidate < low:
                    candidate += int("1" * length)
                elif low <= candidate <= high:
                    out.append(candidate)
                    candidate += int("1" * length)
                elif candidate > high:
                    break

        return out
