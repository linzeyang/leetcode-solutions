"""118. Pascal's Triangle"""

from typing import Generator, List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return list(gen(numRows))


def gen(n: int) -> Generator[list, None, None]:
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
