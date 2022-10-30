"""2451. Odd String Difference"""

from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        dic: dict[tuple[int], list[str]] = {}

        for word in words:
            diff = self.get_diff(word)

            if diff not in dic:
                if dic and len(list(dic.values())[0]) > 1:
                    return word
                dic[diff] = [word]
            else:
                if len(dic) == 1:
                    dic[diff].append(word)
                else:
                    for k, v in dic.items():
                        if k != diff:
                            return v[0]

    def get_diff(self, word: str) -> tuple[int]:
        return tuple((ord(word[i]) - ord(word[i - 1])) for i in range(1, len(word)))
