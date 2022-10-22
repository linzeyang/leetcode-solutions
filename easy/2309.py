"""2309. Greatest English Letter in Upper and Lower Case"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        dic = {}

        for char in s:
            if char.islower():
                char = char.upper()
                if char not in dic:
                    dic[char] = 0
                elif dic[char] == 1:
                    dic[char] = 2
            else:
                if char not in dic:
                    dic[char] = 1
                elif dic[char] == 0:
                    dic[char] = 2

        ll = [char for char, val in dic.items() if val == 2]

        if not ll:
            return ""

        return max(ll)
