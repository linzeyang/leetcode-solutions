"""
3909. Compare Sums of Bitonic Parts

https://leetcode.com/problems/compare-sums-of-bitonic-parts/

Biweekly Contest 181
"""


class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        current_peak: int = nums[0]
        prefix_sum: int = nums[0]
        prefix_at_peak: int = prefix_sum

        for idx in range(1, len(nums)):
            num: int = nums[idx]
            prefix_sum += num

            if num > current_peak:
                current_peak = num
                prefix_at_peak = prefix_sum

        left: int = prefix_at_peak - current_peak
        right: int = prefix_sum - prefix_at_peak

        if left > right:
            return 0

        if left < right:
            return 1

        return -1
