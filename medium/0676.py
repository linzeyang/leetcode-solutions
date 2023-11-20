"""676. Implement Magic Dictionary"""

from typing import List


class MagicDictionary:
    def __init__(self):
        self._tree: dict[int, set[str]] = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            if len(word) not in self._tree:
                self._tree[len(word)] = {word}
            else:
                self._tree[len(word)].add(word)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self._tree:
            return False

        for word in self._tree[len(searchWord)]:
            if self._distance(word, searchWord):
                return True

        return False

    def _distance(self, word1: str, word2: str) -> int:
        count = 0

        for idx, char in enumerate(word1):
            if char != word2[idx]:
                count += 1
                if count > 1:
                    return 0

        return count
