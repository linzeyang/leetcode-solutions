"""
9. Palindrome Number
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        string = str(x)

        for i in range(len(string) // 2):
            if string[i] != string[-i - 1]:
                return False

        return True
