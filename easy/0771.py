"""771. Jewels and Stones"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ss = set(jewels)
        return len([_ for _ in stones if _ in ss])
