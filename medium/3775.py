"""3775. Reverse Words With Same Vowel Count"""


class Solution:
    def reverseWords(self, s: str) -> str:
        if " " not in s:
            return s

        words: list[str] = s.split(" ")
        temp: list[str] = [words[0]]

        def count_vowels(word: str) -> int:
            return sum(1 for char in word if char in "aeiou")

        def reverse_word(word: str) -> str:
            return word[::-1]

        target: int = count_vowels(word=words[0])

        for idx in range(1, len(words)):
            if count_vowels(word=words[idx]) == target:
                temp.append(reverse_word(word=words[idx]))
            else:
                temp.append(words[idx])

        return " ".join(temp)
