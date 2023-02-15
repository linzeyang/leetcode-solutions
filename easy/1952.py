"""1952. Three Divisors"""


class Solution:
    def isThree(self, n: int) -> bool:
        if n in {1, 2, 3, 5, 7}:
            return False

        if n == 4:
            return True

        if n % 2 == 0:
            return False

        if int(n**0.5) ** 2 != n:
            return False

        return self.is_prime(int(n**0.5))

    def is_prime(self, num: int) -> bool:
        if num in {2, 3, 5, 7, 11, 13}:
            return True

        if num % 2 == 0:
            return False

        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False

        return True
