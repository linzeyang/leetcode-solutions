"""
3945. Digit Frequency Score

https://leetcode.com/problems/digit-frequency-score/

Weekly Contest 504
"""

from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        counter: Counter[str] = Counter(str(n))

        return sum(int(char) * freq for char, freq in counter.items())
