"""1104. Path In Zigzag Labelled Binary Tree"""

from math import log2
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]

        if label < 4:
            return [1, label]

        power = int(log2(label))

        prev = 2 ** (power - 1) + 2**power - 1 - label // 2

        return self.pathInZigZagTree(prev) + [label]
