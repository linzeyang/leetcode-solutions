"""
374. Guess Number Higher or Lower
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    ...


class Solution:
    def guessNumber(self, n: int) -> int:
        # Very slow:
        # Runtime: 68 ms, faster than 5.25% of Python3 online submissions for Guess Number Higher or Lower.
        # Memory Usage: 14 MB, less than 15.99% of Python3 online submissions for Guess Number Higher or
        if n == 1:
            return 1

        start, i, end = 1, n // 2, n

        while (r := guess(num=i)) != 0:
            if r == -1:
                end = i
                new_i = (start + i) // 2
                if new_i == i:
                    i = new_i - 1
                else:
                    i = new_i
            else:
                start = i
                new_i = (i + end) // 2
                if new_i == i:
                    i = new_i + 1
                else:
                    i = new_i

        return i
