"""1518. Water Bottles"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        out = empty = numBottles

        while empty >= numExchange:
            batches, rem = divmod(empty, numExchange)
            out += batches
            empty = batches + rem

        return out
