"""263. Ugly Number"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True

        if n < 1:
            return False

        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False

        return True
