"""1780. Check if Number is a Sum of Powers of Three"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            div, mod = divmod(n, 3)

            if mod == 2:
                return False

            n = div

        return True
