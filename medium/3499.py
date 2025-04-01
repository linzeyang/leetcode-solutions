"""3499. Maximize Active Section with Trade I"""


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        length = len(s)

        if length < 3:
            return s.count("1")

        sections: list[int] = []

        count = 1

        for idx in range(1, length):
            if s[idx] == s[idx - 1]:
                count += 1
            else:
                sections.append(count)
                count = 1

        sections.append(count)

        if (s.startswith("0") and len(sections) < 3) or (
            s.startswith("1") and len(sections) < 4
        ):
            return s.count("1")

        if s.startswith("0"):
            section_idx = 1
        else:
            section_idx = 2

        max_converted = 0

        while section_idx < len(sections) - 1:
            converted = sections[section_idx - 1] + sections[section_idx + 1]
            max_converted = max(max_converted, converted)

            section_idx += 2

        return max_converted + s.count("1")


if __name__ == "__main__":
    testcases: tuple[tuple[tuple[str], int], ...] = (
        (("01",), 1),
        (("0100",), 4),
        (("1000100",), 7),
        (("01010",), 4),
        (("10100101",), 7),
        (("010101100",), 7),
    )

    solution = Solution()

    for case in testcases:
        assert solution.maxActiveSectionsAfterTrade(*case[0]) == case[1]
