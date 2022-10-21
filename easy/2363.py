"""2363. Merge Similar Items"""

from typing import List


class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        dic = dict(items1)

        for v, w in items2:
            if v not in dic:
                dic[v] = w
            else:
                dic[v] += w

        return sorted(dic.items(), key=lambda tup: tup[0])
