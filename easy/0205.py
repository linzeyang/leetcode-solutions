"""205. Isomorphic Strings"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 1:
            return True

        temp = {}

        for idx, char in enumerate(s):
            if char not in temp:
                if t[idx] in temp.values():
                    return False

                temp[char] = t[idx]
            elif temp[char] != t[idx]:
                return False

        return True
