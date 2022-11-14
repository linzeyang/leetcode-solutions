"""2399. Check Distances Between Same Letters"""

from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic = {}

        for idx, char in enumerate(s):
            if char not in dic:
                dic[char] = idx
            elif distance[ord(char) - ord("a")] != idx - dic[char] - 1:
                return False

        return True
