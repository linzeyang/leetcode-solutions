"""3456. Find Special Substring of Length K"""


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        counter = 1
        char = s[0]

        idx = 1

        while idx < len(s):
            if s[idx] == char:
                counter += 1
            else:
                if counter == k:
                    return True

                char = s[idx]
                counter = 1
            idx += 1

        if counter == k:
            return True

        return False
