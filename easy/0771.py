"""771. Jewels and Stones"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for stone in stones if stone in set(jewels))
