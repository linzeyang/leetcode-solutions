"""500. Keyboard Row"""

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        mapping = {
            0: "qwertyuiop",
            1: "asdfghjkl",
            2: "zxcvbnm",
        }

        out: list[str] = []

        for word in words:
            initial = word[0].lower()

            target = 0 if initial in mapping[0] else 1 if initial in mapping[1] else 2

            for idx in range(1, len(word)):
                char = word[idx].lower()

                current = 0 if char in mapping[0] else 1 if char in mapping[1] else 2

                if current != target:
                    break
            else:
                out.append(word)

        return out
