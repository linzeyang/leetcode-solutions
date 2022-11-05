"""1450. Number of Students Doing Homework at a Given Time"""

from typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        return len([x for x, y in zip(startTime, endTime) if x <= queryTime <= y])
