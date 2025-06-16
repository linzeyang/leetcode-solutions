"""3582. Generate Tag for Video Caption"""


class Solution:
    def generateTag(self, caption: str) -> str:
        words: list[str] = caption.strip().split(" ")

        words[0] = words[0].lower()

        for idx in range(1, len(words)):
            words[idx] = words[idx].title()

        return ("#" + "".join(words))[:100]
