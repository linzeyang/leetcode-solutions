"""1816. Truncate Sentence"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for idx, char in enumerate(s):
            if char == " ":
                if k > 1:
                    k -= 1
                else:
                    return s[:idx]
        return s
