"""3783. Mirror Distance of an Integer"""


class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))
