"""208. Implement Trie (Prefix Tree)"""


class Trie:
    def __init__(self):
        self._tree: dict[str, list[str]] = {}

    def insert(self, word: str) -> None:
        if word[0] not in self._tree:
            self._tree[word[0]] = [word]
        else:
            self._tree[word[0]].append(word)

    def search(self, word: str) -> bool:
        if word[0] not in self._tree:
            return False

        return word in self._tree[word[0]]

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self._tree:
            return False

        for word in self._tree[prefix[0]]:
            if word.startswith(prefix):
                return True

        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
