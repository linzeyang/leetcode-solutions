"""13. Roman to Integer"""


class Solution:
    def romanToInt(self, s: str) -> int:
        out = idx = 0

        while idx < len(s):
            char = s[idx]

            if char == "M":
                out += 1_000
            elif char == "D":
                out += 500
            elif char == "L":
                out += 50
            elif char == "V":
                out += 5
            elif char == "C":
                if idx + 1 < len(s):
                    if s[idx + 1] == "D":
                        out += 400
                        idx += 2
                        continue
                    elif s[idx + 1] == "M":
                        out += 900
                        idx += 2
                        continue
                    else:
                        out += 100
                else:
                    out += 100
            elif char == "X":
                if idx + 1 < len(s):
                    if s[idx + 1] == "L":
                        out += 40
                        idx += 2
                        continue
                    elif s[idx + 1] == "C":
                        out += 90
                        idx += 2
                        continue
                    else:
                        out += 10
                else:
                    out += 10
            elif char == "I":
                if idx + 1 < len(s):
                    if s[idx + 1] == "V":
                        out += 4
                        idx += 2
                        continue
                    elif s[idx + 1] == "X":
                        out += 9
                        idx += 2
                        continue
                    else:
                        out += 1
                else:
                    out += 1

            idx += 1

        return out
