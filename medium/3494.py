"""3494. Find the Minimum Amount of Time to Brew Potions"""

from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        len_skill = len(skill)
        len_mana = len(mana)

        prev: list[int] = [0]

        for idx in range(len_skill):
            prev.append(prev[-1] + skill[idx] * mana[0])

        for jdx in range(1, len_mana):
            current: list[int] = [prev[1]]

            for idx in range(len_skill):
                current.append(current[-1] + skill[idx] * mana[jdx])

            max_diff = max(
                prev[idx] - current[idx - 1] for idx in range(1, len_skill + 1)
            )

            for idx in range(len_skill + 1):
                current[idx] += max_diff

            prev = current

        return prev[-1]
