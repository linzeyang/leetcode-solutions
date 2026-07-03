"""
3975. Filter Occupied Intervals

https://leetcode.com/problems/filter-occupied-intervals/

Weekly Contest 508
"""

from typing import List


class Solution:
    def filterOccupiedIntervals(
        self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int
    ) -> List[List[int]]:
        occupiedIntervals.sort(key=lambda intervals: (intervals[0], intervals[1]))
        merged_intervals: list[list[int]] = []

        for intervals in occupiedIntervals:
            if not merged_intervals:
                merged_intervals.append(intervals)
                continue

            last_interval: list[int] = merged_intervals[-1]

            if intervals[0] - last_interval[1] <= 1:
                last_interval[1] = max(last_interval[1], intervals[1])
            else:
                merged_intervals.append(intervals)

        if freeStart > merged_intervals[-1][1] or freeEnd < merged_intervals[0][0]:
            return merged_intervals

        out: list[list[int]] = []

        for start, end in merged_intervals:
            if start > freeEnd or end < freeStart:
                out.append([start, end])
                continue

            if start < freeStart:
                out.append([start, freeStart - 1])

                if end > freeEnd:
                    out.append([freeEnd + 1, end])

            elif end > freeEnd:
                out.append([freeEnd + 1, end])

        return out
