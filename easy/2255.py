"""2255. Count Prefixes of a Given String"""

from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([w for w in words if w == s[: len(w)]])
