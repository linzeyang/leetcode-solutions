"""3121. Count the Number of Special Characters II"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mapping: dict[str, list[int]] = {}
        invalid: set[str] = set()

        for char in word:
            low = char.lower()
            is_low = int(char.islower())

            if low not in mapping:
                mapping[low] = [0, 0]

            if is_low:
                if mapping[low][1]:
                    invalid.add(low)
                else:
                    mapping[low][0] = 1
            else:
                mapping[low][1] = 1

        count = 0

        for k, val in mapping.items():
            if val[0] == val[1] == 1 and k not in invalid:
                count += 1

        return count
