"""1534. Count Good Triplets"""

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        out = 0

        for idx in range(len(arr) - 2):
            for jdx in range(idx + 1, len(arr) - 1):
                if abs(arr[idx] - arr[jdx]) > a:
                    continue

                for kdx in range(jdx + 1, len(arr)):
                    if abs(arr[jdx] - arr[kdx]) > b or abs(arr[idx] - arr[kdx]) > c:
                        continue

                    out += 1

        return out
