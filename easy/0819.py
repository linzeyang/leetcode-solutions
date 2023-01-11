"""819. Most Common Word"""

import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pattern = re.compile(r"[!?',;.]")

        dic = {}

        for word in paragraph.split():
            for sub_word in word.split(","):
                if not sub_word:
                    continue

                sub_word = re.sub(pattern, "", sub_word.strip()).lower()

                if sub_word not in banned:
                    if sub_word not in dic:
                        dic[sub_word] = 1
                    else:
                        dic[sub_word] += 1

        target = max(dic.values())

        for word, count in dic.items():
            if count == target:
                return word

        return ""
