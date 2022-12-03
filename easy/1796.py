"""1796. Second Largest Digit in a String"""


class Solution:
    def secondHighest(self, s: str) -> int:
        temp: set[str] = set()

        for char in s:
            if char.isdigit():
                if len(temp) < 2:
                    temp.add(char)
                elif char not in temp and char > min(temp):
                    temp = {max(temp), char}

        if len(temp) < 2:
            return -1

        return int(min(temp))
