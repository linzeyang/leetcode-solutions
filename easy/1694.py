"""1694. Reformat Phone Number"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        temp: list[str] = []

        while len(number) > 4:
            temp.append(number[:3])
            number = number[3:]

        if len(number) == 4:
            temp.append(number[:2])
            temp.append(number[2:])
        elif len(number) in {2, 3}:
            temp.append(number)

        return "-".join(temp)
