"""2446. Determine if Two Events Have Conflict"""

from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return not (event1[1] < event2[0]) and not (event1[0] > event2[1])
