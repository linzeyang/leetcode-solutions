"""278. First Bad Version"""


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    ...


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n

        while start < end:
            pick = (start + end) // 2

            if isBadVersion(pick):
                end = pick
            else:
                start = pick + 1

        return end
