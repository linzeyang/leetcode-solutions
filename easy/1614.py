"""1614. Maximum Nesting Depth of the Parentheses"""


class Solution:
    def maxDepth(self, s: str) -> int:
        temp = []
        out = 0

        for char in s:
            if char == "(":
                temp.append(char)
                length = len(temp)
                if length > out:
                    out = length
            elif char == ")":
                temp.pop()

        return out
