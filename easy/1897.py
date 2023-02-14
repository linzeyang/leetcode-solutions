"""1897. Redistribute Characters to Make All Strings Equal"""

from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        temp = Counter("".join(words))

        for count in temp.values():
            if count % length != 0:
                return False

        return True
