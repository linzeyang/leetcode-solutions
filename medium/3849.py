"""3849. Maximum Bitwise XOR After Rearrangement"""

from collections import Counter


class Solution:
    """
    https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/
    Weekly Contest 490
    """

    def maximumXor(self, s: str, t: str) -> str:
        temp: list[str] = []

        counter: Counter[str] = Counter(t)

        for bit in s:
            if bit == "0":
                if counter["1"]:
                    temp.append("1")
                    counter["1"] -= 1
                else:
                    temp.append("0")
                    counter["0"] -= 1
            else:
                if counter["0"]:
                    temp.append("0")
                    counter["0"] -= 1
                else:
                    temp.append("1")
                    counter["1"] -= 1

        return "".join("1" if a != b else "0" for a, b in zip(s, temp, strict=True))
