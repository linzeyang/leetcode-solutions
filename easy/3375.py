"""3375. Minimum Operations to Make Array Values Equal to K"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        all_num = set(nums)

        if k > min(all_num):
            return -1

        return sum(1 for num in all_num if num > k)


if __name__ == "__main__":
    testcases: tuple[tuple[tuple[list[int], int], int], ...] = (
        (([5, 2, 5, 4, 5], 2), 2),
        (([2, 1, 2], 2), -1),
        (([9, 7, 5, 3], 1), 4),
        (([5, 2, 5, 4, 5], 6), -1),
        (([5, 2, 5, 4, 5], 3), -1),
        (([5, 2, 5, 4, 5], 1), 3),
    )

    solution = Solution()

    for case in testcases:
        assert solution.minOperations(*case[0]) == case[1]
