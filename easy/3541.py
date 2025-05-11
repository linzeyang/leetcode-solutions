"""3541. Find Most Frequent Vowel and Consonant"""


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vols: dict[str, int] = {}
        cons: dict[str, int] = {}

        for char in s:
            if char in "aeiou":
                if char not in vols:
                    vols[char] = 1
                else:
                    vols[char] += 1
            else:
                if char not in cons:
                    cons[char] = 1
                else:
                    cons[char] += 1

        return max(vols.values(), default=0) + max(cons.values(), default=0)
