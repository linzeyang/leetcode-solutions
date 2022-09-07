"""
27. Remove Element
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        if (length := len(nums)) == 1:
            if nums[0] == val:
                return 0
            return length

        head_ind = 0
        tail_ind = len(nums) - 1

        while head_ind < tail_ind:
            if nums[head_ind] != val:
                head_ind += 1
            else:
                while tail_ind > head_ind:
                    if nums[tail_ind] != val:
                        nums[head_ind] = nums[tail_ind]
                        nums[tail_ind] = val
                        tail_ind -= 1
                        break
                    tail_ind -= 1

        if nums[head_ind] != val:
            return head_ind + 1
        return head_ind
