"""804. Unique Morse Code Words"""

from typing import List

CODES = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len({self.transform(word) for word in words})

    def transform(self, word: str) -> str:
        return "".join(CODES[ord(char) - ord("a")] for char in word)
