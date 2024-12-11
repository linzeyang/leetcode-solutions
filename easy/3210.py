"""3210. Find the Encrypted String"""


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k %= len(s)

        return "".join(s[(idx + k) % len(s)] for idx in range(len(s)))
