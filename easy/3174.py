"""3174. Clear Digits"""


class Solution:
    def clearDigits(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            if not char.isdigit():
                stack.append(char)
            elif stack:
                stack.pop()

        return "".join(stack)
