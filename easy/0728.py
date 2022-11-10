"""728. Self Dividing Numbers"""

from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right + 1) if self._is_self_dividing(num)]

    def _is_self_dividing(self, num: int) -> bool:
        for char in str(num):
            if char == "1":
                continue
            if char == "0" or num % int(char):
                return False

        return True
