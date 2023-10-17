"""748. Shortest Completing Word"""

from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate_set = {char.lower() for char in licensePlate if char.isalpha()}
        plate_counter = Counter(char.lower() for char in licensePlate if char.isalpha())

        completing_word = ""

        for word in words:
            if not plate_set.issubset(set(word)):
                continue

            for char, count in Counter(word).items():
                if char not in plate_set:
                    continue

                if count < plate_counter[char]:
                    break
            else:
                if completing_word == "" or len(word) < len(completing_word):
                    completing_word = word

        return completing_word
