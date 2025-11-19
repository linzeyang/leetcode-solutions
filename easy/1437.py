"""1437. Check If All 1's Are at Least Length K Places Away"""

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return True

        current: int = -1

        for idx, num in enumerate(nums):
            if not num:
                continue

            if current >= 0 and idx - current <= k:
                return False

            current = idx

        return True
