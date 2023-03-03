"""520. Detect Capital"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.isupper():
            return True

        return word.istitle()
