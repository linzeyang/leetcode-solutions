"""3477. Fruits Into Baskets II"""

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        out = 0

        for fru in fruits:
            for idx, bas in enumerate(baskets):
                if bas >= fru:
                    baskets.pop(idx)
                    break
            else:
                out += 1

        return out


if __name__ == "__main__":
    testcases: list[tuple] = [
        ([[4, 2, 5], [3, 5, 4]], 1),
        ([[3, 6, 1], [6, 4, 7]], 0),
    ]

    for tup in testcases:
        assert Solution().numOfUnplacedFruits(*tup[0]) == tup[1]
