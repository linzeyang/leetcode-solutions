"""2396. Strictly Palindromic Number"""


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            base_repr = self._base_repr(n, base)

            if base_repr != base_repr[::-1]:
                return False

        return True

    def _base_repr(self, n: int, base: int) -> list[int]:
        _repr: list[int] = []

        while n > 0:
            n, mod = divmod(n, base)
            _repr.append(mod)

        return _repr
