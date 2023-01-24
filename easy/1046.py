"""1046. Last Stone Weight"""

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones = sorted(stones)

        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                new = stones[-1] - stones[-2]
                stones.pop()
                stones[-1] = new
                stones = sorted(stones)

        if not stones:
            return 0

        return stones[0]
