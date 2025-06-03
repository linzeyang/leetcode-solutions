"""762. Prime Number of Set Bits in Binary Representation"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        out = 0
        primes: set[int] = {2, 3, 5, 7, 11, 13, 17, 19}

        for num in range(left, right + 1):
            num_of_one = bin(num).count("1")

            if num_of_one in primes:
                out += 1

        return out
