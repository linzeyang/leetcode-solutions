"""868. Binary Gap"""


class Solution:
    """
    https://leetcode.com/problems/binary-gap/
    Weekly Contest 93
    """

    def binaryGap(self, n: int) -> int:
        bin_form: str = bin(n)[2:]
        prev_one: int = -1
        max_distance = 0

        for idx, char in enumerate(bin_form):
            if char == "1":
                if prev_one >= 0 and (distance := idx - prev_one) > max_distance:
                    max_distance = distance
                prev_one = idx

        return max_distance


class Solution2:
    def binaryGap(self, n: int) -> int:
        one_idxs: list[int] = [idx for idx, bit in enumerate(f"{n:b}") if bit == "1"]

        if len(one_idxs) < 2:
            return 0

        return max(one_idxs[jdx] - one_idxs[jdx - 1] for jdx in range(1, len(one_idxs)))
