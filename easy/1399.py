"""1399. Count Largest Group"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        temp = {}

        for num in range(1, n + 1):
            if (summ := self._digit_sum(num)) not in temp:
                temp[summ] = 1
            else:
                temp[summ] += 1

        maxx = max(temp.values())

        return len([_ for _, v in temp.items() if v == maxx])

    def _digit_sum(self, num: int) -> int:
        return sum(int(char) for char in str(num))
