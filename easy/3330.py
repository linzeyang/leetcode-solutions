"""3330. Find the Original Typed String I"""


class Solution:
    def possibleStringCount(self, word: str) -> int:
        out = 1

        last_digit = word[0]

        counter = 1

        for idx in range(1, len(word)):
            if word[idx] == last_digit:
                counter += 1
            else:
                if counter != 1:
                    out += counter - 1

                last_digit = word[idx]
                counter = 1

        if counter != 1:
            out += counter - 1

        return out
