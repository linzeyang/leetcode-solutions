"""
3941. Password Strength

https://leetcode.com/problems/password-strength/

Weekly Contest 503
"""


class Solution:
    def passwordStrength(self, password: str) -> int:
        unique_chars: set[str] = set(password)

        out: int = 0

        for char in unique_chars:
            if char.islower():
                out += 1
            elif char.isupper():
                out += 2
            elif char.isdigit():
                out += 3
            else:
                out += 5

        return out
