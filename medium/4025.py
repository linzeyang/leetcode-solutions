"""
4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights

https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/

Weekly Contest 515
"""


class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        max_light: int = max(lights)
        out: int = 0

        for time in arrivalTime:
            time %= period

            if time >= max_light:
                out = max(out, period - time)

        return out
