"""2683. Neighboring Bitwise XOR"""

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_sum = derived[0]

        for idx in range(1, len(derived)):
            xor_sum ^= derived[idx]

        return xor_sum == 0
