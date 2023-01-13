"""844. Backspace String Compare"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self._type(s) == self._type(t)

    def _type(self, sentence: str) -> str:
        temp = []

        for char in sentence:
            match char:
                case "#":
                    try:
                        temp.pop()
                    except IndexError:
                        ...
                case _:
                    temp.append(char)

        return "".join(temp)
