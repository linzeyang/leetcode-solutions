"""3767. Maximize Points After Choosing K Tasks"""

from typing import List


class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        ordered_pairs: list[tuple[int, int]] = sorted(
            zip(technique1, technique2, strict=True),
            key=lambda tup: tup[0] - tup[1],
            reverse=True,
        )

        out: int = 0

        for idx, tup in enumerate(ordered_pairs):
            if idx < k:
                out += tup[0]
            else:
                out += max(tup[0], tup[1])

        return out
