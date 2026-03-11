"""1009. Complement of Base 10 Integer"""


class Solution:
    """
    https://leetcode.com/problems/complement-of-base-10-integer/
    Weekly Contest 128
    Note that this is the same as 476.
    """

    def bitwiseComplement(self, n: int) -> int:
        return 2 ** len(f"{n:b}") - 1 - n
