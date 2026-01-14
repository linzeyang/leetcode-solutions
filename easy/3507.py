"""3507. Minimum Pair Removal to Sort Array I"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
    Weekly Contest 444
    """

    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(arr: list[int]) -> bool:
            """Check if array is sorted in non-decreasing order."""

            return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

        if len(nums) <= 1 or is_sorted(nums):
            return 0

        operations: int = 0

        while not is_sorted(nums):
            # Find the adjacent pair with minimum sum
            min_sum: int = 100_000
            min_idx: int = 0

            for i in range(1, len(nums)):
                pair_sum: int = nums[i] + nums[i - 1]

                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i - 1

            # Remove the pair and insert their sum
            nums[min_idx] = min_sum
            nums.pop(min_idx + 1)

            operations += 1

        return operations


def test_solution():
    """Test cases for the solution."""

    sol = Solution()

    # Test case 1: Already sorted array
    assert sol.minimumPairRemoval([1, 2, 3, 4]) == 0

    # Test case 2: Single element
    assert sol.minimumPairRemoval([5]) == 0

    # Test case 3: Simple unsorted array - takes 1 operation
    # (sum 2+1=3, array becomes [3,3] which is sorted)
    assert sol.minimumPairRemoval([3, 2, 1]) == 1

    # Test case 4: Mixed array - takes 1 operation
    # (sum 2+1=3, array becomes [3,3,4] which is sorted)
    assert sol.minimumPairRemoval([2, 1, 3, 4]) == 1

    # Test case 5: Mixed array - takes 2 operations
    assert sol.minimumPairRemoval([5, 2, 3, 1]) == 2

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
