"""3663. Find The Least Frequent Digit"""

from collections import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counter: Counter[str] = Counter(str(n))

        min_freq: int = min(counter.values())

        candidates: list[str] = [key for key, val in counter.items() if val == min_freq]

        return int(min(candidates))
