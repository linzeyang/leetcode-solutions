"""1021. Remove Outermost Parentheses"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        out = []
        temp = []

        for char in s:
            if char == "(" and not temp:
                temp.append(char)
            elif char == ")" and len(temp) == 1:
                temp.pop()
            elif char == "(":
                temp.append(char)
                out.append(char)
            else:
                temp.pop()
                out.append(char)

        return "".join(out)
