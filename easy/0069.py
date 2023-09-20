"""69. Sqrt(x)"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x

        while right - left > 1:
            mid = (left + right) // 2

            if mid**2 == x:
                return mid

            if mid**2 > x:
                right = mid
            else:
                left = mid

        return left
