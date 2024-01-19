"""953. Verifying an Alien Dictionary"""

from string import ascii_lowercase
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = dict(zip(order, ascii_lowercase, strict=False))

        alt_list = ["".join(dic[letter] for letter in word) for word in words]

        return sorted(alt_list) == alt_list
