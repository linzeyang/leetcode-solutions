"""1769. Minimum Number of Operations to Move All Balls to Each Box"""

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = [idx for idx in range(len(boxes)) if boxes[idx] == "1"]

        return [sum(abs(one - i) for one in ones) for i in range(len(boxes))]
