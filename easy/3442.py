"""3442. Maximum Difference Between Even and Odd Frequency I"""


class Solution:
    def maxDifference(self, s: str) -> int:
        counter: dict[str, int] = {}

        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        odd_max = 0
        even_min = 100

        for val in counter.values():
            if val & 1 == 1 and val > odd_max:
                odd_max = val
            elif val & 1 == 0 and val < even_min:
                even_min = val

        return odd_max - even_min
