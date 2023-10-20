"""20. Valid Parentheses"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        MATCHING = {(")", "("), ("}", "{"), ("]", "[")}

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False

                if (char, stack[-1]) in MATCHING:
                    stack.pop()
                else:
                    return False

        return not stack
