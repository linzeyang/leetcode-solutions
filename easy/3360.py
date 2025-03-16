"""3360. Stone Removal Game"""


class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        target = 10
        is_alice = True

        while n >= target:
            n -= target
            target -= 1
            is_alice = not is_alice

        return not is_alice
