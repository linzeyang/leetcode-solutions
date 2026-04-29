"""
3913. Sort Vowels by Frequency

https://leetcode.com/problems/sort-vowels-by-frequency/

Weekly Contest 499
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        chars: list[str] = list(s)
        counter: dict[str, list[int]] = {}

        for idx, char in enumerate(chars):
            if char not in "aeiou":
                continue

            if char not in counter:
                counter[char] = [1, idx]
            else:
                counter[char][0] += 1

        sorted_vowels: list[str] = sorted(
            counter.keys(), key=lambda vowel: (-counter[vowel][0], counter[vowel][1])
        )

        for idx, char in enumerate(chars):
            if char not in "aeiou":
                continue

            for vowel in sorted_vowels:
                if counter[vowel][0] > 0:
                    chars[idx] = vowel
                    counter[vowel][0] -= 1
                    break

        return "".join(chars)
