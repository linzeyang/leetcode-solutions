"""3829. Design Ride Sharing System"""

from collections import deque
from typing import List


class RideSharingSystem:
    """
    https://leetcode.com/problems/design-ride-sharing-system/
    Weekly Contest 487
    """

    def __init__(self):
        self.riderq: deque[int] = deque()
        self.driverq: deque[int] = deque()

    def addRider(self, riderId: int) -> None:
        self.riderq.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driverq.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.driverq and self.riderq:
            return [self.driverq.popleft(), self.riderq.popleft()]

        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riderq:
            self.riderq.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
