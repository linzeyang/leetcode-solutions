"""3146. Permutation Difference between Two Strings"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        mapping: dict[str, int] = {char: idx for idx, char in enumerate(s)}

        return sum(abs(idx - mapping[char]) for idx, char in enumerate(t))
