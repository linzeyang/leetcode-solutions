"""3238. Find the Number of Winning Players"""

from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        mapping: dict[int, dict[int, int]] = {}

        for player, color in pick:
            if player not in mapping:
                mapping[player] = {color: 1}
            elif color not in mapping[player]:
                mapping[player][color] = 1
            else:
                mapping[player][color] += 1

        out = 0

        for player in range(n):
            if player not in mapping:
                continue

            if max(mapping[player].values()) > player:
                out += 1

        return out
