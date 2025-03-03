"""3468. Find the Number of Copy Arrays"""

from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        lower_bound, upper_bound = bounds[0]

        for idx in range(1, len(original)):
            diff = original[idx] - original[idx - 1]

            lower_bound += diff
            upper_bound += diff

            if lower_bound > bounds[idx][1] or upper_bound < bounds[idx][0]:
                return 0

            lower_bound = max(lower_bound, bounds[idx][0])
            upper_bound = min(upper_bound, bounds[idx][1])

        return upper_bound - lower_bound + 1
