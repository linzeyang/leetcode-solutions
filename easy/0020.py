"""
20. Valid Parentheses
"""


class Solution:
    def isValid(self, s: str) -> bool:
        opened_stack = []

        for char in s:
            if char in OPENING:
                opened_stack.append(char)
            else:
                try:
                    last_opened = opened_stack.pop()
                except IndexError:
                    return False
                if MAPPING[char] != last_opened:
                    return False

        return len(opened_stack) == 0


MAPPING = {
    "}": "{",
    "]": "[",
    ")": "(",
}
OPENING = {"(", "[", "{"}
