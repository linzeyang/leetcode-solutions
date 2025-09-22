"""1935. Maximum Number of Words You Can Type"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set: set[str] = set(brokenLetters)

        return sum(1 for word in text.split() if not set(word) & broken_set)
