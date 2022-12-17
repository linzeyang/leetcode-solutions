"""1629. Slowest Key"""

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        dic = {keysPressed[0]: releaseTimes[0]}

        for idx in range(1, len(keysPressed)):
            if (char := keysPressed[idx]) not in dic:
                dic[char] = releaseTimes[idx] - releaseTimes[idx - 1]
            else:
                dic[char] = max(dic[char], releaseTimes[idx] - releaseTimes[idx - 1])

        keys = [k for k, v in dic.items() if v == max(dic.values())]

        return max(keys)
