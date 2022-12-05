"""2490. Circular Sentence"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        start = prev = None

        for word in sentence.split():
            if start is None:
                start = word

            if prev is None:
                prev = word
                continue

            if prev[-1] != word[0]:
                return False

            prev = word

        return word[-1] == start[0]
