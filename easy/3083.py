"""3083. Existence of a Substring in a String and Its"""


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        choices: set[str] = {s[idx : idx + 2] for idx in range(len(s) - 1)}

        rev_choices: set[str] = {
            s[-idx - 1 : -idx - 3 : -1] for idx in range(len(s) - 1)
        }

        for choice in choices:
            if choice in rev_choices:
                return True

        return False
