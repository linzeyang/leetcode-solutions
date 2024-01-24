"""343. Integer Break"""


class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        div, mod = divmod(n, 3)

        out = 3**div

        if mod == 1:
            out = out // 3 * 4
        elif mod == 2:
            out *= 2

        return out
