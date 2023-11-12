"""2928. Distribute Candies Among Children I"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        temp: set[tuple[int, int, int]] = set()

        for idx in range(min(n, limit) + 1):
            for jdx in range(min(n - idx, limit) + 1):
                kdx = n - idx - jdx

                if kdx <= limit:
                    temp.add((idx, jdx, kdx))

        return len(temp)
