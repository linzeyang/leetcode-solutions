"""1441. Build an Array With Stack Operations"""

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out: list[str] = []
        stream_idx = 1

        for num in target:
            while num != stream_idx:
                out.append("Push")
                out.append("Pop")
                stream_idx += 1

            out.append("Push")
            stream_idx += 1

        return out
