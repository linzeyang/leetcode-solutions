"""3285. Find Indices of Stable Mountains"""

from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [idx for idx in range(1, len(height)) if height[idx - 1] > threshold]
