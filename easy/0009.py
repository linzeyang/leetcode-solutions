"""
9. Palindrome Number
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        string = list(str(x))

        for i in range(int(len(string) / 2)):
            if string[i] != string[len(string) - i - 1]:
                return False

        return True
