"""2080. Range Frequency Queries"""

from bisect import bisect_left, bisect_right
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.freqs: dict = {}

        for idx, num in enumerate(arr):
            if num not in self.freqs:
                self.freqs[num] = [idx]
            else:
                self.freqs[num].append(idx)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.freqs:
            return 0

        left_bound = bisect_left(self.freqs[value], left)
        right_bound = bisect_right(self.freqs[value], right)

        return right_bound - left_bound
