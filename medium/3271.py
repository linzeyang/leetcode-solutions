"""3271. Hash Divided String"""


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        return "".join(self._hash(s[idx : idx + k]) for idx in range(0, len(s), k))

    def _hash(self, sequence: str) -> str:
        return chr(sum(ord(char) - ord("a") for char in sequence) % 26 + ord("a"))
