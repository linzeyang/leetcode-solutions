"""3016. Minimum Number of Pushes to Type Word II"""

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(
            counts * (idx // 8 + 1)
            for idx, counts in enumerate(sorted(Counter(word).values(), reverse=True))
        )
