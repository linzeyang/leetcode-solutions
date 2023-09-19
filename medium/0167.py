"""167. Two Sum II - Input Array Is Sorted"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while (summ := numbers[left] + numbers[right]) != target:
            if summ > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]
