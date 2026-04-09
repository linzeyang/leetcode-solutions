"""
3890. Integers With Multiple Sum of Two Cubes

https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

Weekly Contest 496
"""

from collections import Counter


class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        cuberoot = int(n ** (1 / 3))
        cubes: list[int] = [idx**3 for idx in range(1, cuberoot + 1)]

        counter: Counter[int] = Counter()

        for idx in range(1, cuberoot + 1):
            a_cube: int = cubes[idx - 1]
            target: int = n - a_cube

            for jdx in range(idx + 1, cuberoot + 1):
                b_cube: int = cubes[jdx - 1]

                if b_cube > target:
                    break

                counter[a_cube + b_cube] += 1

        return sorted(key for key, val in counter.items() if val >= 2)
