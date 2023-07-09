"""1387. Sort Integers by The Power Value"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted(range(lo, hi + 1), key=self._get_power)[k - 1]

    def _get_power(self, num: int) -> int:
        if num == 1:
            return 0

        count = 0

        while num != 1:
            if num % 2:
                num = num * 3 + 1
            else:
                num //= 2

            count += 1

        return count
