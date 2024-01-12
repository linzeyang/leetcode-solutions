"""389. Find the Difference"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if t.count(char) != s.count(char):
                return char

        return ""


class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        out = list(t)

        for char in s:
            out.remove(char)

        return out[0]


class Solution3:
    def findTheDifference(self, s: str, t: str) -> str:
        mapping_s = {}
        mapping_t = {}

        for char in s:
            if char not in mapping_s:
                mapping_s[char] = 1
            else:
                mapping_s[char] += 1

        for char in t:
            if char not in mapping_s:
                return char

            if char not in mapping_t:
                mapping_t[char] = 1
            else:
                mapping_t[char] += 1

            if mapping_t[char] > mapping_s[char]:
                return char

        return ""
