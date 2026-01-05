"""3794. Reverse String Prefix"""


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[k - 1 :: -1] + s[k:]
