"""3314. Construct the Minimum Bitwise Array I"""

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        out: list[int] = []

        for num in nums:
            if num == 2:
                out.append(-1)
                continue

            bits = list(f"{num:b}")

            for idx in range(1, len(bits) + 1):
                if bits[-idx] == "0":
                    break
            else:
                idx = 0

            if idx == 0:
                bits[0] = "0"
            else:
                bits[-idx + 1] = "0"

            out.append(int("".join(bits), base=2))

        return out
