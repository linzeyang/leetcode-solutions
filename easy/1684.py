"""1684. Count the Number of Consistent Strings"""

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ss = set(allowed)
        return len([word for word in words if set(word).issubset(ss)])
