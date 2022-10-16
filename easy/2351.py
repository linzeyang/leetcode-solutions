"""2351. First Letter to Appear Twice"""


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ss = set()

        for char in s:
            if char not in ss:
                ss.add(char)
            else:
                return char
