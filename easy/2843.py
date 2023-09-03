"""2843. Count Symmetric Integers"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(1 for num in range(low, high + 1) if self._is_symm(num))

    def _is_symm(self, num: int) -> bool:
        str_num = str(num)

        if (len_num := len(str_num)) % 2:
            return False

        digits = list(str_num)

        return sum(int(char) for char in digits[: len_num // 2]) == sum(
            int(char) for char in digits[len_num // 2 :]
        )
