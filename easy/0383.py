"""383. Ransom Note"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_mapping = {}

        for char in magazine:
            if char not in mag_mapping:
                mag_mapping[char] = 1
            else:
                mag_mapping[char] += 1

        ran_mapping = {}

        for char in ransomNote:
            if char not in magazine:
                return False

            if char not in ran_mapping:
                ran_mapping[char] = 1
            else:
                ran_mapping[char] += 1

            if ran_mapping[char] > mag_mapping[char]:
                return False

        return True
