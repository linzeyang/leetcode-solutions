"""1641. Count Sorted Vowel Strings"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5

        temp = [1, 1, 1, 1, 1]

        for _ in range(n - 1):
            temp = [temp[0], sum(temp[:2]), sum(temp[:3]), sum(temp[:4]), sum(temp[:5])]

        return sum(temp)
