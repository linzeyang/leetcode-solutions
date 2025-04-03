"""2873. Maximum Value of an Ordered Triplet I"""

from typing import List


# constraint: 3 <= nums.length <= 100
class Solution:
    """Time-complexity: O(N)"""

    def maximumTripletValue(self, nums: List[int]) -> int:
        head_maxs: list[int] = [nums[0]]

        for idx in range(1, len(nums)):
            head_maxs.append(max(nums[idx], head_maxs[-1]))

        tail_maxs: list[int] = [nums[-1]]

        for idx in range(2, len(nums) + 1):
            tail_maxs.append(max(nums[-idx], tail_maxs[-1]))

        tail_maxs = tail_maxs[::-1]

        out = 0

        for idx in range(1, len(nums) - 1):
            out = max(out, (head_maxs[idx - 1] - nums[idx]) * tail_maxs[idx + 1])

        return out


if __name__ == "__main__":
    testcases: tuple[tuple[tuple[list[int]], int], ...] = (
        (([12, 6, 1, 2, 7],), 77),
        (([1, 10, 3, 4, 19],), 133),
        (([1, 2, 3],), 0),
    )

    for case in testcases:
        assert Solution().maximumTripletValue(*case[0]) == case[1]
