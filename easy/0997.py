""""""

from collections import Counter
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1

        if len(trust) == 1:
            if max(trust[0]) == 2:
                return trust[0][1]
            else:
                return -1

        trust_map = Counter(t[1] for t in trust)

        candidates = [k for k, v in trust_map.items() if v == n - 1]

        if len(candidates) != 1:
            return -1

        candidate = candidates[0]

        temp = {t[0] for t in trust}

        if candidate in temp:
            return -1

        return candidate
