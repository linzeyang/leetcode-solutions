"""1015. Smallest Integer Divisible by K"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k & 1 == 0 or k % 5 == 0:
            return -1  # even numbers or ???5 would never divide 1???1

        mod: int = 1 % k
        out: int = 1

        while mod:
            # use modulo to keep the number within the range of 0 ~ k-1
            mod = (mod * 10 + 1) % k
            out += 1

        return out
