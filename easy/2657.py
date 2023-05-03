"""2657. Find the Prefix Common Array of Two Arrays"""

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seta = set()
        setb = set()

        out = []

        for idx in range(len(A)):
            seta.add(A[idx])
            setb.add(B[idx])

            out.append(len(seta & setb))

        return out
