"""
20. Valid Parentheses

https://leetcode.cn/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        MATCHING: set[tuple[str, str]] = {(")", "("), ("}", "{"), ("]", "[")}

        for char in s:
            if char in "({[":
                stack.append(char)
            elif not stack or (char, stack[-1]) not in MATCHING:
                return False
            else:
                stack.pop()

        return not stack
