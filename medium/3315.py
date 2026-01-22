"""3315. Construct the Minimum Bitwise Array II"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/
    Biweekly Contest 141
    """

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        out: list[int] = []

        for num in nums:
            if num == 2:  # The only even number that is also a prime is 2
                out.append(-1)
            else:
                binary: str = bin(num)[2:]
                # For odd num with least-significant zero at bit position q,
                # subtract 2^(q-1)
                out.append(num - 2 ** (len(binary) - binary.rfind("0") - 2))

        return out
