"""1961. Check If String Is a Prefix of Array"""

from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        len_s = len(s)

        aggre = 0

        for _idx, word in enumerate(words):
            aggre += len(word)

            if aggre == len_s:
                break

            if aggre > len_s:
                return False
        else:
            return False

        return s == "".join(words[: _idx + 1])
