"""3206. Alternating Groups I"""

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        out = 0

        for idx in range(len(colors)):
            left = idx - 1 if idx > 0 else len(colors) - 1
            right = idx + 1 if idx < len(colors) - 1 else 0

            if colors[left] == colors[right] and colors[idx] != colors[left]:
                out += 1

        return out
