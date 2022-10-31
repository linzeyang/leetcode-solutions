"""1832. Check if the Sentence Is Pangram"""

from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(ascii_lowercase).issubset(set(sentence))
