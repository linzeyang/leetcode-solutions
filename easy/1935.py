"""1935. Maximum Number of Words You Can Type"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)

        return len([word for word in text.split() if self._can_type(word, broken)])

    def _can_type(self, word: str, broken: set[str]) -> bool:
        return not bool(set(word) & broken)
