"""2785. Sort Vowels in a String"""


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels: list[str] = []
        vowel_indexes: list[int] = []

        VOS = "aeiou"

        for idx, letter in enumerate(s):
            if letter.lower() in VOS:
                vowels.append(letter)
                vowel_indexes.append(idx)

        s_list = list(s)

        for idx, letter in zip(vowel_indexes, sorted(vowels), strict=False):
            s_list[idx] = letter

        return "".join(s_list)
