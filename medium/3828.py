"""3828. Final Element After Subarray Deletions"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/final-element-after-subarray-deletions/
    Weekly Contest 487
    """

    def finalElement(self, nums: List[int]) -> int:
        """
        Alice can choose to end the game immediately by removing all elements except
        nums[0] or nums[-1]. Since Bob plays optimally to minimize the result,
        Alice cannot do better by passing the turn. Therefore, the optimal strategy
        for Alice is to take the maximum of the two ends.
        """

        return max(nums[0], nums[-1])
