"""3136. Valid Word"""


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels: str = "aeiouAEIOU"

        num_of_vowel = num_of_cons = 0

        for char in word:
            if not char.isalnum():
                return False

            if char in vowels:
                num_of_vowel += 1
            elif char.isalpha():
                num_of_cons += 1

        return False if (num_of_vowel < 1 or num_of_cons < 1) else True
