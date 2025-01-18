"""3095. Shortest Subarray With OR at Least K I"""

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        length = len(nums)

        out = -1

        for idx in range(length):
            if nums[idx] >= k:
                if out == -1 or out > 1:
                    out = 1
            else:
                sub = nums[idx]

                for j in range(idx + 1, length):
                    sub |= nums[j]

                    if sub >= k:
                        sub_len = j - idx + 1

                        if out == -1 or sub_len < out:
                            out = sub_len

                        break

        return out
