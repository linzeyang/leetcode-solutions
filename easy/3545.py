"""3545. Minimum Deletions for At Most K Distinct Characters"""

from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter: Counter = Counter(s)

        if len(counter) <= k:
            return 0

        sorted_key: list[str] = sorted(
            counter.keys(), key=lambda char: counter[char], reverse=True
        )

        return sum(counter[key] for key in sorted_key[k:])
