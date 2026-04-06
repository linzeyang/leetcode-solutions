"""
3885. Design Event Manager

https://leetcode.com/problems/design-event-manager/

Weekly Contest 495
"""

import heapq


class EventManager:
    def __init__(self, events: list[list[int]]):
        self.heap: list[tuple[int, int]] = [
            (-priority, eid) for eid, priority in events
        ]
        heapq.heapify(self.heap)

        self.event_priority: dict[int, int] = {}

        for eid, priority in events:
            self.event_priority[eid] = priority

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.event_priority[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            neg_priority, eid = heapq.heappop(self.heap)

            if eid not in self.event_priority:
                continue

            if -neg_priority == self.event_priority[eid]:
                del self.event_priority[eid]
                return eid

        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
