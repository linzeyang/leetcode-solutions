"""
118. Pascal's Triangle
"""
from typing import Generator, List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return list(gen(numRows))


def gen(n: int) -> Generator[list, None, None]:
    # Slow:
    # Runtime: 60 ms, faster than 18.02% of Python3 online submissions for Pascal's Triangle.
    # Memory Usage: 13.9 MB, less than 65.61% of Python3 online submissions for Pascal's Triangle.
    out = []

    for j in range(n):
        if not out:
            out.append(1)
        else:
            new = []
            for i in range(j + 1):
                if i == 0 or i == j:
                    new.append(1)
                else:
                    new.append(out[i - 1] + out[i])
            out = new
        yield out
