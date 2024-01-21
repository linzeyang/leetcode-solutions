"""3014. Minimum Number of Pushes to Type Word I"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        num = len(word)

        if num <= 8:
            return num

        if num <= 16:
            return 8 + 2 * (num - 8)

        if num <= 24:
            return 24 + 3 * (num - 16)

        return 48 + 4 * (num - 24)
