"""1207. Unique Number of Occurrences"""

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cc = Counter(arr)

        return len(cc) == len(set(cc.values()))
