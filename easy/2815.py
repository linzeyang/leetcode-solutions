"""2815. Max Pair Sum in an Array"""

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mapping: dict[int, list[int]] = {}

        for num in nums:
            maxx = self._get_max_digit(num)

            if maxx not in mapping:
                mapping[maxx] = [num]
            else:
                mapping[maxx].append(num)

        out = 0

        for sub_nums in mapping.values():
            if len(sub_nums) < 2:
                continue

            sub_nums.sort()

            sub_maxx = sub_nums[-1] + sub_nums[-2]

            if sub_maxx > out:
                out = sub_maxx

        return out if out else -1

    def _get_max_digit(self, num: int) -> int:
        if num < 10:
            return num

        return int(max(list(str(num))))
