"""2810. Faulty Keyboard"""


class Solution:
    def finalString(self, s: str) -> str:
        temp = []

        for char in s:
            if char == "i":
                temp.reverse()
            else:
                temp.append(char)

        return "".join(temp)
