"""
412. Fizz Buzz
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Very slow:
        # Runtime: 100 ms, faster than 5.65% of Python3 online submissions for Fizz Buzz.
        # Memory Usage: 15.1 MB, less than 17.74% of Python3 online submissions for Fizz Buzz.
        return [
            "FizzBuzz"
            if i % 15 == 0
            else "Fizz"
            if i % 3 == 0
            else "Buzz"
            if i % 5 == 0
            else str(i)
            for i in range(1, n + 1)
        ]
