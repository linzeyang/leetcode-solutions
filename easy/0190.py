"""190. Reverse Bits"""


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{f'{n:b}':0>32}"[::-1], base=2)
