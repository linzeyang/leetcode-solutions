"""2125. Number of Laser Beams in a Bank"""

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp = []

        for line in bank:
            count = line.count("1")
            if count:
                temp.append(count)

        if len(temp) <= 1:
            return 0

        out = 0

        for idx in range(len(temp) - 1):
            out += temp[idx] * temp[idx + 1]

        return out
