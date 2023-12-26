"""135. Candy"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1

        out = [1] * len(ratings)

        for idx in range(1, len(ratings)):
            if ratings[idx] > ratings[idx - 1]:
                out[idx] = out[idx - 1] + 1

        for idx in range(len(ratings) - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1] and out[idx] <= out[idx + 1]:
                out[idx] = out[idx + 1] + 1

        return sum(out)
