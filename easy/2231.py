"""2231. Largest Number After Digit Swaps by Parity"""


class Solution:
    def largestInteger(self, num: int) -> int:
        str_num: str = str(num)

        temp: list[str] = [""] * len(str_num)

        odds_map: dict[int, str] = {}
        evens_map: dict[int, str] = {}

        for idx, char in enumerate(str_num):
            if int(char) % 2 == 1:
                odds_map[idx] = char
            else:
                evens_map[idx] = char

        for idx, num in zip(
            list(odds_map.keys()), sorted(odds_map.values(), reverse=True), strict=False
        ):
            temp[idx] = num

        for idx, num in zip(
            list(evens_map.keys()),
            sorted(evens_map.values(), reverse=True),
            strict=False,
        ):
            temp[idx] = num

        return int("".join(temp))
