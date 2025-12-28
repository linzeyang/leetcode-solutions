"""3789. Minimum Cost to Acquire Required Items"""


class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        if cost1 + cost2 < costBoth:
            return cost1 * need1 + cost2 * need2

        base: int = min(need1, need2) * costBoth

        if need1 > need2:
            return base + (need1 - need2) * min(cost1, costBoth)

        return base + (need2 - need1) * min(cost2, costBoth)
