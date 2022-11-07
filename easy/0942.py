"""942. DI String Match"""

from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ll = sorted(range(len(s) + 1))
        out = []

        for char in s:
            if char == "I":
                out.append(ll.pop(0))
            else:
                out.append(ll.pop())

        out.append(ll[0])

        return out
