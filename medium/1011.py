"""1011. Capacity To Ship Packages Within D Days"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            actual_days = 1
            accumulated = 0

            for weight in weights:
                accumulated += weight

                if accumulated > mid:
                    actual_days += 1
                    accumulated = weight

            if actual_days > days:
                left = mid + 1
            else:
                right = mid

        return left
