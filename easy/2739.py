"""2739. Total Distance Traveled"""


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        out = 0

        while mainTank >= 5:
            out += 50
            mainTank -= 5

            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1

        out += mainTank * 10

        return out
