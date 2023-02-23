"""2264. Largest 3-Same-Digit Number in String"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        temp = set()

        for idx in range(2, len(num)):
            if num[idx] == num[idx - 1] == num[idx - 2]:
                temp.add(num[idx])

        return max(temp) * 3 if temp else ""
