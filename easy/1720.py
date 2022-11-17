"""1720. Decode XORed Array"""

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out = [first]

        for num in encoded:
            out.append(out[-1] ^ num)

        return out
