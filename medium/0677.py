"""677. Map Sum Pairs"""


class MapSum:
    def __init__(self):
        self._trie: dict[str, dict[str, int]] = {}

    def insert(self, key: str, val: int) -> None:
        if key[0] not in self._trie:
            self._trie[key[0]] = {key: val}
        else:
            self._trie[key[0]][key] = val

    def sum(self, prefix: str) -> int:
        out = 0

        if prefix[0] not in self._trie:
            return out

        for key, val in self._trie[prefix[0]].items():
            if key.startswith(prefix):
                out += val

        return out


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
