"""3169. Count Days Without Meetings"""

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda lis: lis[0])

        segments: list[list[int]] = []

        for start, end in meetings:
            if not segments:
                segments.append([start, end])
                continue

            if start <= segments[-1][1] + 1:
                segments[-1][1] = max(segments[-1][1], end)
            else:
                segments.append([start, end])

        out = days

        for start, end in segments:
            out -= end - start + 1

        return out
