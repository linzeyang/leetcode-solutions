"""3438. Find Valid Pair of Adjacent Digits in String"""


class Solution:
    def findValidPair(self, s: str) -> str:
        counter = {}

        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                continue

            if counter[s[idx]] == int(s[idx]) and counter[s[idx + 1]] == int(
                s[idx + 1]
            ):
                return s[idx : idx + 2]

        return ""
