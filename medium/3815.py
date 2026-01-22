"""3815. Design Auction System"""

import heapq
from collections import defaultdict


class AuctionSystem:
    """
    https://leetcode.com/problems/design-auction-system/
    Weekly Contest 485
    """

    def __init__(self) -> None:
        # itemId -> userId -> bidAmount
        self.records: dict[int, dict[int, int]] = defaultdict(dict)
        # itemId -> list of (-bidAmount, -userId)
        self.heaps: dict[int, list[tuple[int, int]]] = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.records[itemId][userId] = bidAmount
        heapq.heappush(self.heaps[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId=userId, itemId=itemId, bidAmount=newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        if userId in self.records[itemId]:
            del self.records[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        h: list[tuple[int, int]] = self.heaps[itemId]

        out: int = -1

        while h:
            bid, uid = -h[0][0], -h[0][1]

            # Check if this bid is valid (matches current record)
            if self.records[itemId].get(uid) == bid:
                out = uid
                break

            # If not valid (stale or removed), remove from heap
            heapq.heappop(h)

        return out


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
