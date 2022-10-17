"""2283. Check if Number Has Equal Digit Count and Digit Value"""


from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        cc = Counter(num)

        for idx, digit in enumerate(num):
            if cc[str(idx)] != int(digit):
                return False

        return True
