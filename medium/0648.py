"""648. Replace Words"""

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree: dict[str, list[str]] = {}

        for word in dictionary:
            if word[0] not in tree:
                tree[word[0]] = [word]
            else:
                tree[word[0]].append(word)

        for lis in tree.values():
            lis.sort()

        return " ".join(self._replace(word, tree) for word in sentence.split(" "))

    def _replace(self, word, tree) -> str:
        if word[0] not in tree:
            return word

        for wor in tree[word[0]]:
            if word.startswith(wor):
                return wor

        return word
