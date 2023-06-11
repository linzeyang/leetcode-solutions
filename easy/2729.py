"""2729. Check if The Number is Fascinating"""


class Solution:
    def isFascinating(self, n: int) -> bool:
        if n > 333:
            return False

        gen = f"{n}{n * 2}{n * 3}"

        return len(set(gen)) == 9 and "0" not in gen
