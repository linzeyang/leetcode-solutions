"""
125. Valid Palindrome
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Slow:
        # Runtime: 106 ms, faster than 18.25% of Python3 online submissions for Valid Palindrome.
        # Memory Usage: 14.5 MB, less than 56.90% of Python3 online submissions for Valid Palindrome.
        length = len(s)
        out = True

        head = 0
        tail = length - 1

        while head < tail:
            while (head <= length - 1) and not s[head].isalnum():
                head += 1
            while (tail >= 0) and not s[tail].isalnum():
                tail -= 1

            if (head > length - 1) or (tail < 0):
                break

            if s[head].lower() != s[tail].lower():
                return False

            head += 1
            tail -= 1

        return out
