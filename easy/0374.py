"""374. Guess Number Higher or Lower"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int: ...


class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n

        while start < end:
            pick = (start + end) // 2

            if (result := guess(pick)) == 0:
                return pick

            if result == -1:
                end = pick - 1
            else:
                start = pick + 1

        return start
