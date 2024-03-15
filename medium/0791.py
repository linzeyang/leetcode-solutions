"""791. Custom Sort String"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mapping = {char: idx for idx, char in enumerate(order)}

        temp: list[str | None] = [None] * len(mapping)
        counter: dict = {}
        remaining = []

        for char in s:
            if char not in mapping:
                remaining.append(char)
            else:
                if char not in counter:
                    counter[char] = 1

                    temp[mapping[char]] = char
                else:
                    counter[char] += 1

        out = []

        for char in temp:
            if char is not None:
                out.append(char * counter[char])

        out.extend(remaining)

        return "".join(out)
