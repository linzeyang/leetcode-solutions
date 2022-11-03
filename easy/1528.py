"""1528. Shuffle String"""

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join(
            tupl[0] for tupl in sorted(zip(s, indices), key=lambda tup: tup[1])
        )
