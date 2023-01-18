"""868. Binary Gap"""


class Solution:
    def binaryGap(self, n: int) -> int:
        bin_form = bin(n)[2:]
        prev_one = -1
        max_distance = 0

        for idx, char in enumerate(bin_form):
            if char == "1":
                if prev_one >= 0 and (distance := idx - prev_one) > max_distance:
                    max_distance = distance
                prev_one = idx

        return max_distance
