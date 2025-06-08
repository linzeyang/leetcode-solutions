"""3572. Maximize Y-Sum by Picking a Triplet of Distinct X-Values"""

from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        num_to_idxs: dict[int, list[int]] = {}

        for idx, num in enumerate(x):
            if num not in num_to_idxs:
                num_to_idxs[num] = [idx]
            else:
                num_to_idxs[num].append(idx)

        if len(num_to_idxs) < 3:
            return -1

        num_to_max_y: dict[int, int] = {}

        for num, idxs in num_to_idxs.items():
            num_to_max_y[num] = max(y[idx] for idx in idxs)

        return sum(sorted(num_to_max_y.values(), reverse=True)[:3])
