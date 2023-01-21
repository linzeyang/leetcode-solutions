"""888. Fair Candy Swap"""

from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)

        diff = abs(sum_a - sum_b) // 2

        if sum_a < sum_b:
            set_a = set(aliceSizes)
            set_b = set(bobSizes)
        else:
            set_a = set(bobSizes)
            set_b = set(aliceSizes)

        answer = []

        for num in set_a:
            if num + diff in set_b:
                answer = [num, num + diff]

        if sum_a > sum_b:
            return list(reversed(answer))

        return answer
