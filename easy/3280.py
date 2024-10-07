"""3280. Convert Date to Binary"""


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(f"{int(part):b}" for part in date.split("-"))
