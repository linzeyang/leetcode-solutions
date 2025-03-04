"""1652. Defuse the Bomb"""

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        out: list[int] = []

        if k > 0:
            out.append(sum(code[1 : k + 1]))

            left = 1
            right = (1 + k) % len(code)
        else:
            out.append(sum(code[k:]))

            left = k
            right = 0

        for _ in range(len(code) - 1):
            out.append(out[-1] - code[left] + code[right])
            left = (left + 1) % len(code)
            right = (right + 1) % len(code)

        return out
