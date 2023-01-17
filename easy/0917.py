"""917. Reverse Only Letters"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        out: list[str] = []
        letter_iter = (char for char in reversed(s) if char.isalpha())

        for char in s:
            if not char.isalpha():
                out.append(char)
            else:
                out.append(next(letter_iter))

        return "".join(out)
