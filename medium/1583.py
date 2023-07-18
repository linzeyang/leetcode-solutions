"""1583. Count Unhappy Friends"""

from typing import List


class Solution:
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        out = 0

        pair_mapping: dict[int, int] = {}

        for per1, per2 in pairs:
            pair_mapping[per1] = per2
            pair_mapping[per2] = per1

        for per1, per2 in pairs:
            per1_pref = preferences[per1]

            if per2 != per1_pref[0]:
                idx = 0

                while (other_per := per1_pref[idx]) != per2:
                    print(f"{other_per=}")
                    other_per_paired_per = pair_mapping[other_per]

                    other_per_pref = preferences[other_per]

                    if other_per_pref.index(per1) < other_per_pref.index(
                        other_per_paired_per
                    ):
                        out += 1
                        break

                    idx += 1

            per2_pref = preferences[per2]

            if per1 != per2_pref[0]:
                idx = 0

                while (other_per := per2_pref[idx]) != per1:
                    other_per_paired_per = pair_mapping[other_per]

                    other_per_pref = preferences[other_per]

                    if other_per_pref.index(per2) < other_per_pref.index(
                        other_per_paired_per
                    ):
                        out += 1
                        break

                    idx += 1

        return out


def test_solution_case_1():
    assert (
        Solution().unhappyFriends(
            n=4,
            preferences=[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]],
            pairs=[[0, 1], [2, 3]],
        )
        == 2
    )


def test_solution_case_2():
    assert (
        Solution().unhappyFriends(
            n=6,
            preferences=[
                [1, 4, 3, 2, 5],
                [0, 5, 4, 3, 2],
                [3, 0, 1, 5, 4],
                [2, 1, 4, 0, 5],
                [2, 1, 0, 3, 5],
                [3, 4, 2, 0, 1],
            ],
            pairs=[[3, 1], [2, 0], [5, 4]],
        )
        == 5
    )
