"""3340. Check Balanced String"""


class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_even = sum(int(num[idx]) for idx in range(0, len(num), 2))

        sum_odd = sum(int(num[idx]) for idx in range(1, len(num), 2))

        return sum_even == sum_odd
