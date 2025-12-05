"""3623. Count Number of Trapezoids I"""

import math
from collections import Counter
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # Count points at each y-coordinate
        y_counts: Counter[int] = Counter(y for _, y in points)

        # Calculate number of horizontal pairs at each y-level
        # and incrementally update sums for the final calculation
        total_sum: int = 0
        sum_sq: int = 0

        for count in y_counts.values():
            if count > 1:
                pairs: int = math.comb(count, 2)
                total_sum += pairs
                sum_sq += pairs**2

        if not total_sum:
            return 0

        # We want to calculate: sum_{i < j} (count[i] * count[j])
        # Using the identity: (sum(a))^2 = sum(a^2) + 2 * sum_{i < j} (a_i * a_j)
        # Therefore: sum_{i < j} (a_i * a_j) = ((sum(a))^2 - sum(a^2)) // 2

        return ((total_sum**2 - sum_sq) // 2) % (10**9 + 7)
