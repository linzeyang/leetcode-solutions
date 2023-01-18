"""884. Uncommon Words from Two Sentences"""

from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic = {}

        for word in s1.split(" ") + s2.split(" "):
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

        return [word for word, count in dic.items() if count == 1]
