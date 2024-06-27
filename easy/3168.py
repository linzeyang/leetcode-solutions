"""3168. Minimum Number of Chairs in a Waiting Room"""


class Solution:
    def minimumChairs(self, s: str) -> int:
        stack: list = []
        out = 0

        for char in s:
            match char:
                case "E":
                    stack.append(None)
                case "L":
                    stack.pop()

            if len(stack) > out:
                out = len(stack)

        return out
