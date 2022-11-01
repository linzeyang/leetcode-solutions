"""1221. Split a String in Balanced Strings"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        temp = []
        count = 0

        for char in s:
            if not temp or temp[-1] == char:
                temp.append(char)
            else:
                temp.pop()

            if not temp:
                count += 1

        return count
