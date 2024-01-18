"""873. Length of Longest Fibonacci Subsequence"""

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        sset: set[int] = set(arr)
        memory: set[tuple[int, int, int]] = set()
        out = 0

        for idx in range(len(arr) - 2):
            for jdx in range(idx + 1, len(arr) - 1):
                a, b = arr[idx], arr[jdx]
                lenn = 0

                while a + b in sset:
                    if (a, b, a + b) not in memory:
                        memory.add((a, b, a + b))
                    else:
                        break

                    if not lenn:
                        lenn = 3
                    else:
                        lenn += 1
                    a, b = b, a + b

                if lenn > out:
                    out = lenn

        return out
