"""2299. Strong Password Checker II"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lower = upper = digit = special = False

        specials = "!@#$%^&*()-+"

        for idx, char in enumerate(password):
            if (idx < len(password) - 1) and char == password[idx + 1]:
                return False

            if char.isupper():
                if not upper:
                    upper = True
            elif char.islower():
                if not lower:
                    lower = True
            elif char.isdigit():
                if not digit:
                    digit = True
            elif char in specials:
                if not special:
                    special = True

        return lower and upper and digit and special
