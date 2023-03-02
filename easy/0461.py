"""461. Hamming Distance"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Another solution:
        # x_str = f"{x:0>31b}"
        # y_str = f"{y:0>31b}"

        # out = 0

        # for idx, char in enumerate(x_str):
        #     if char != y_str[idx]:
        #         out += 1

        # return out

        return bin(x ^ y).count("1")
