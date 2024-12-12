"""3370. Smallest Number With All Set Bits"""


class Solution:
    def smallestNumber(self, n: int) -> int:
        length = len(f"{n:b}")

        return int("1" * length, base=2)
