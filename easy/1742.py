"""1742. Maximum Number of Balls in a Box"""


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = {}

        for num in range(lowLimit, highLimit + 1):
            if (box := self._which_box(num)) not in dic:
                dic[box] = 1
            else:
                dic[box] += 1

        return max(dic.values())

    def _which_box(self, number: int) -> int:
        return sum(int(char) for char in str(number))
