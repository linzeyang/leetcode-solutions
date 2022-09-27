"""415. Add Strings"""


# This violates the rule: You must also not convert the inputs to integers directly.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Runtime: 36 ms, faster than 96.33% of Python3 online submissions for Add Strings.
        # Memory Usage: 13.9 MB, less than 88.54% of Python3 online submissions for Add Strings.
        return str(int(num1) + int(num2))
