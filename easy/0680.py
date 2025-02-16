"""680. Valid Palindrome II"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if self._is_palindrome(s[left + 1 : right + 1]) or self._is_palindrome(
                    s[left:right]
                ):
                    return True

                return False

        return True

    def _is_palindrome(self, sub: str) -> bool:
        return sub == sub[-1::-1]
