"""1358. Number of Substrings Containing All Three Characters"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        out = 0

        counter = {
            "a": s[:3].count("a"),
            "b": s[:3].count("b"),
            "c": s[:3].count("c"),
        }

        left, right = 0, 2

        for idx in range(len(s) - 2):
            left = idx

            while right < len(s):
                if not counter["a"] or not counter["b"] or not counter["c"]:
                    right += 1
                    if right < len(s):
                        counter[s[right]] += 1
                else:
                    break

            out += len(s) - right

            if len(s) - right == 0:
                return out

            counter[s[left]] -= 1

        return out
