"""2433. Find The Original Array of Prefix Xor"""

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[idx - 1] ^ pref[idx] for idx in range(1, len(pref))]
