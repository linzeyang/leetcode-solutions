"""435. Non-overlapping Intervals"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda interval: interval[1])
        num_keep = 1
        ending = intervals[0][1]

        for idx in range(1, len(intervals)):
            if intervals[idx][0] < ending:
                continue

            ending = intervals[idx][1]
            num_keep += 1

        return len(intervals) - num_keep
