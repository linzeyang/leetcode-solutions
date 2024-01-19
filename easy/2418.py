"""2418. Sort the People"""

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [
            tu[0]
            for tu in sorted(
                zip(names, heights, strict=False), key=lambda tup: tup[-1], reverse=True
            )
        ]
