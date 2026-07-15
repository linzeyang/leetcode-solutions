"""
3986. Number of Elapsed Seconds Between Two Times

https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

Weekly Contest 510
"""


class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start_h, start_m, start_s = (int(part) for part in startTime.split(":"))

        end_h, end_m, end_s = (int(part) for part in endTime.split(":"))

        return (end_h - start_h) * 3600 + (end_m - start_m) * 60 + (end_s - start_s)
