"""1436. Destination City"""

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = dict(paths)

        for val in dic.values():
            if val not in dic:
                return val
