"""1957. Delete Characters to Make Fancy String"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        chars: list[str] = [s[0]]

        counter = 1

        for idx in range(1, len(s)):
            if s[idx] != chars[-1]:
                chars.append(s[idx])
                counter = 1
            elif counter == 1:
                chars.append(s[idx])
                counter += 1

        return "".join(chars)
