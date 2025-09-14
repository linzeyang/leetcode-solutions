"""3683. Earliest Time to Finish One Task"""

from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(s + t for s, t in tasks)
