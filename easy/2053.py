"""2053. Kth Distinct String in an Array"""

from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}

        for word in arr:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

        counter = 0

        for word, val in dic.items():
            if val == 1:
                counter += 1
                if counter == k:
                    return word

        return ""
