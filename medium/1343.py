"""1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold

        left = right = count = summ = 0

        while right < len(arr):
            summ += arr[right]

            if right - left < k - 1:
                right += 1
            else:
                if summ >= target:
                    count += 1

                summ -= arr[left]

                left += 1
                right += 1

        return count
