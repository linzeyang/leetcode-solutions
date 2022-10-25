"""1880. Check if Word Equals Summation of Two Words"""


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.evaluate(firstWord) + self.evaluate(secondWord) == self.evaluate(
            targetWord
        )

    def evaluate(self, word: str) -> int:
        return int("".join(str(ord(char) - ord("a")) for char in word))
