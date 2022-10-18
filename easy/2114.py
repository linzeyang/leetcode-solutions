"""2114. Maximum Number of Words Found in Sentences"""

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sen.split()) for sen in sentences)
