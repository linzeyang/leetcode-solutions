"""2997. Minimum Number of Operations to Make Array XOR Equal to K"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = nums[0]

        for num in nums[1:]:
            xor ^= num

        return bin(xor ^ k).count("1")
