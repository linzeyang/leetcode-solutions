"""3114. Latest Time You Can Obtain After Replacing Characters"""


class Solution:
    def findLatestTime(self, s: str) -> str:
        if "?" not in s:
            return s

        lis = list(s)

        if lis[0] == "?":
            if lis[1] == "?" or lis[1] < "2":
                lis[0] = "1"
            else:
                lis[0] = "0"

        if lis[1] == "?":
            if lis[0] == "0":
                lis[1] = "9"
            else:
                lis[1] = "1"

        if lis[3] == "?":
            lis[3] = "5"

        if lis[4] == "?":
            lis[4] = "9"

        return "".join(lis)


if __name__ == "__main__":
    testcases: tuple[tuple[tuple[str], str], ...] = (
        (("1?:?4",), "11:54"),
        (("0?:5?",), "09:59"),
        (("?3:12",), "03:12"),
        (("00:00",), "00:00"),
        (("??:??",), "11:59"),
    )

    solution = Solution()

    for case in testcases:
        assert solution.findLatestTime(*case[0]) == case[1]
