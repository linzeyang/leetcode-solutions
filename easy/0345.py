"""
345. Reverse Vowels of a String
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        # Runtime: 119 ms, faster than 29.77% of Python3 online submissions for Reverse Vowels of a String.
        # Memory Usage: 15 MB, less than 57.69% of Python3 online submissions for Reverse Vowels of a String.
        vowels = frozenset("AEIOUaeiou")
        lis = list(s)
        i, j = 0, len(lis) - 1

        while i < j:
            if lis[i] not in vowels:
                i += 1
                continue

            while i < j:
                if lis[j] not in vowels:
                    j -= 1
                    continue

                lis[i], lis[j] = lis[j], lis[i]
                break

            i += 1
            j -= 1

        return "".join(lis)
