"""482. License Key Formatting"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        num_of_groups, num_of_first_group = divmod(len(s) - s.count("-"), k)

        new_s = "".join(s.split("-")).upper()

        if not num_of_first_group:
            first_group = []
        else:
            first_group = [new_s[:num_of_first_group]]

        groups = first_group + [
            new_s[num_of_first_group + i * k: num_of_first_group + (i + 1) * k]
            for i in range(num_of_groups)
        ]

        return "-".join(groups)
