"""2315. Count Asterisks"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        in_pair = False
        count = 0

        for char in s:
            if char == "|":
                in_pair = not in_pair
            elif char == "*" and not in_pair:
                count += 1

        return count
