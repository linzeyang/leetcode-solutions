"""1859. Sorting the Sentence"""


class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join(word[:-1] for word in sorted(s.split(), key=lambda w: w[-1]))
