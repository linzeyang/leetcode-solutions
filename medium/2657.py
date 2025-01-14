"""2657. Find the Prefix Common Array of Two Arrays"""

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a, set_b = set(), set()

        out: list[int] = []

        for idx in range(len(A)):
            if A[idx] == B[idx]:
                out.append((out[-1] if out else 0) + 1)
            else:
                num = 0

                if A[idx] in set_b:
                    num += 1
                if B[idx] in set_a:
                    num += 1

                out.append((out[-1] if out else 0) + num)

            set_a.add(A[idx])
            set_b.add(B[idx])

        return out
