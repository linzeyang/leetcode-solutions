"""
1021. Remove Outermost Parentheses

https://leetcode.com/problems/remove-outermost-parentheses/

Weekly Contest 131
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        out: list[str] = []
        counter: int = 0

        for char in s:
            if char == "(":
                if counter:
                    out.append(char)

                counter += 1
            else:
                if counter != 1:
                    out.append(char)

                counter -= 1

        return "".join(out)
