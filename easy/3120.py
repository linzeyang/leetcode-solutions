"""3120. Count the Number of Special Characters I"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mapping: dict[str, list[int]] = {}

        for char in word:
            low = char.lower()
            is_low = int(char.islower())

            if low not in mapping:
                mapping[low] = [0, 0]

            mapping[low][is_low] = 1

        count = 0

        for val in mapping.values():
            if val[0] == val[1] == 1:
                count += 1

        return count
