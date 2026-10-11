"""
4078. Three Fibonacci Sum

https://leetcode.com/problems/three-fibonacci-sum/

Weekly Contest 523
"""


class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if n & 1:
            return False

        target: int = n >> 1

        a, b = 0, 1

        while a + b < target:
            a, b = b, a + b

            if a + b > target:
                return False

            if a + b == target:
                return True

        return True
