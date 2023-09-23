"""345. Reverse Vowels of a String"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        lis = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if lis[left] not in vowels:
                left += 1
                continue

            while left < right:
                if lis[right] not in vowels:
                    right -= 1
                    continue

                lis[left], lis[right] = lis[right], lis[left]
                break

            left += 1
            right -= 1

        return "".join(lis)
