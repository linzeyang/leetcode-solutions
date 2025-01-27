"""1409. Queries on a Permutation With Key"""

from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        lis: list[int] = [num + 1 for num in range(m)]

        out: list[int] = []

        for query in queries:
            idx = lis.index(query)

            out.append(idx)

            lis.pop(idx)
            lis.insert(0, query)

        return out
