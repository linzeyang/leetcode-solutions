"""3223. Minimum Length of String After Operations"""

from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)

        return sum(
            value if value < 3 else 1 if value % 2 else 2 for value in counter.values()
        )
