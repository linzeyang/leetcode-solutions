"""2042. Check if Numbers Are Ascending in a Sentence"""


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        base = 0

        for word in s.split():
            if word.isdigit():
                if int(word) > base:
                    base = int(word)
                else:
                    return False

        return True
