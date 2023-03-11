"""1805. Number of Different Integers in a String"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ss = set()
        temp = []

        for char in word:
            if char.islower():
                if temp:
                    ss.add(int("".join(temp)))
                    temp = []
            else:
                temp.append(char)

        if temp:
            ss.add(int("".join(temp)))

        return len(ss)
