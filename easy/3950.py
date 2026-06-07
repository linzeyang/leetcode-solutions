"""
3950. Exactly One Consecutive Set Bits Pair

https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

Biweekly Contest 184
"""


class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        bin_n: str = bin(n)[2:]
        pair_found: bool = False

        for idx in range(1, len(bin_n)):
            if bin_n[idx] == bin_n[idx - 1] == "1":
                if not pair_found:
                    pair_found = True
                else:
                    return False

        return pair_found
