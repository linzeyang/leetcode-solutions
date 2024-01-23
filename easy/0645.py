"""645. Set Mismatch"""

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        array = [0] * len(nums)
        out: list[int] = []

        for num in nums:
            if array[num - 1] == 0:
                array[num - 1] = 1
            else:
                out.append(num)

        for idx, num in enumerate(array):
            if num == 0:
                out.append(idx + 1)
                break

        return out
