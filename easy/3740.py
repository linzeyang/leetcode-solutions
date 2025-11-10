"""3740. Minimum Distance Between Three Equal Elements I"""

from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mapping: defaultdict[int, list[int]] = defaultdict(list)

        for idx, num in enumerate(nums):
            mapping[num].append(idx)

        out: int = -1

        for idx_list in mapping.values():
            if len(idx_list) < 3:
                continue

            candidate: int = (
                min(
                    idx_list[idx] - idx_list[idx - 2] for idx in range(2, len(idx_list))
                )
                * 2
            )

            if out == -1:
                out = candidate
            else:
                out = min(out, candidate)

        return out
