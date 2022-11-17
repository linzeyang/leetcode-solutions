"""1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return idx + 1

        return -1
