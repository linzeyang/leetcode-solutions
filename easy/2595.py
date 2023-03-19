"""2595. Number of Even and Odd Bits"""

from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odd = 0

        for idx, char in enumerate(f"{n:b}"[::-1]):
            if char == "1":
                if idx % 2:
                    odd += 1
                else:
                    even += 1

        return [even, odd]
