"""
4020. Elevator Requests I

https://leetcode.com/problems/elevator-requests-i/

Biweekly Contest 189
"""


class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        out: int = requests[0]

        for idx in range(1, len(requests)):
            out += abs(requests[idx] - requests[idx - 1])

        return out
