"""1009. Complement of Base 10 Integer"""


# Same question as 476
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 2 ** len(f"{n:b}") - 1 - n
