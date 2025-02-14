"""2342. Max Sum of a Pair With Equal Sum of Digits"""

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        out = -1

        mapping: dict[int, list[int]] = {}

        for num in nums:
            summ = self._digit_sum(number=num)

            if summ not in mapping:
                mapping[summ] = [num]
            else:
                mapping[summ].append(num)

        for group in mapping.values():
            if len(group) < 2:
                continue

            add = sum(sorted(group)[-2:])

            out = max(out, add)

        return out

    def _digit_sum(self, number: int) -> int:
        return sum(int(char) for char in str(number))
